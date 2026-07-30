import sys, json, importlib, io, contextlib, shutil
from pathlib import Path
sys.path.insert(0,'scripts'); sys.path.insert(0,'tests')
from fake_wp import FakeWP
from datetime import datetime, timedelta

class FakeResp:
    def __init__(self, d): self._d=d; self.status_code=200; self.headers={}
    def json(self): return self._d
    def raise_for_status(self): pass

def env(wp):
    import wp_client
    class S:
        def get(self, url, params=None, timeout=None):
            params = params or {}
            if url.endswith('/posts'):
                return FakeResp(wp.query(params.get('before'), params.get('page',1), params.get('per_page',100)))
            return FakeResp([])
    wp_client._session=lambda: S()
    wp_client.list_categories=lambda:{1:'News'}
    wp_client.list_all_tags=lambda:{f'Tag{i}':i for i in range(1,9)}
    wp_client.get_post_content=lambda p:'<p>x</p>'
    return wp_client

wp = FakeWP(total=600)
wpc = env(wp)
import fetch_batch; importlib.reload(fetch_batch); fetch_batch.wp_client=wpc
fetch_batch.STATE_PATH=Path('/tmp/s2.json'); fetch_batch.BATCHES_DIR=Path('/tmp/b2')
Path('/tmp/s2.json').unlink(missing_ok=True); shutil.rmtree('/tmp/b2',ignore_errors=True); Path('/tmp/b2').mkdir(parents=True)

def lot(*extra):
    sys.argv=['x','--size','20']+list(extra)
    buf=io.StringIO()
    with contextlib.redirect_stdout(buf): fetch_batch.main()
    st=json.loads(Path('/tmp/s2.json').read_text())
    q=st.get('queued',[])
    for pid in q: wp.tag(pid)
    st['processed']=st.get('processed',[])+q; st['queued']=[]
    Path('/tmp/s2.json').write_text(json.dumps(st))
    return buf.getvalue(), st, q

# 3 lots normaux : on descend dans le backlog
for i in range(3):
    out, st, q = lot()
c_avant = st['scan_cursor']
ids_backlog = st['processed'][-20:]
print(f"Après 3 lots normaux : curseur = {c_avant}")
print(f"  60 articles traités, du plus récent vers l'ancien : ids {st['processed'][0]} -> {st['processed'][-1]}")

# Nouveaux articles publiés (plus récents que tout le reste)
for i in range(5):
    d = datetime(2026,6,1,12,0,0) + timedelta(hours=i+1)
    wp.posts.insert(0, {"id":9000+i, "date":d.isoformat(), "title":{"rendered":f"Nouveau {i}"},
                        "categories":[1], "tags":[]})
print(f"\n5 nouveaux articles publiés (ids 9000-9004), plus récents que le curseur.")

# Mode reprise : ne doit PAS les voir
out, st, q = lot()
print(f"\nLot en mode reprise      -> ids {q}")
print(f"  nouveaux articles inclus ? {any(i>=9000 for i in q)}  (attendu : False)")
print(f"  curseur : {st['scan_cursor']}  (a avancé : {st['scan_cursor']!=c_avant})")
c_apres_reprise = st['scan_cursor']

# Mode --from-top : doit les voir, et ne PAS toucher au curseur
out, st, q = lot('--from-top')
print(f"\nLot en mode --from-top   -> ids {q}")
print(f"  nouveaux articles inclus ? {any(i>=9000 for i in q)}  (attendu : True)")
print(f"  curseur inchangé ? {st['scan_cursor']==c_apres_reprise}  (attendu : True)")
print(f"  curseur : {st['scan_cursor']}")

# Reprise après from-top : doit continuer le backlog là où il était
out, st, q = lot()
print(f"\nReprise après --from-top -> ids {q}")
print(f"  reprend bien dans le backlog (ids < 9000) ? {all(i<9000 for i in q)}  (attendu : True)")