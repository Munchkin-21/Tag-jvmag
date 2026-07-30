"""Simule le tagging complet du catalogue via le pipeline réel (wp_client + fetch_batch)."""
import sys, types, json, importlib
from pathlib import Path
sys.path.insert(0, 'scripts'); sys.path.insert(0, 'tests')
from fake_wp import FakeWP

def make_env(wp):
    """Branche le vrai wp_client sur le faux WordPress (on remplace juste la couche HTTP)."""
    import wp_client
    class FakeResp:
        def __init__(self, data): self._d = data; self.status_code = 200; self.headers = {}
        def json(self): return self._d
        def raise_for_status(self): pass
    class FakeSession:
        def get(self, url, params=None, timeout=None):
            params = params or {}
            if url.endswith('/posts'):
                return FakeResp(wp.query(before=params.get('before'),
                                         page=params.get('page', 1),
                                         per_page=params.get('per_page', 100)))
            return FakeResp([])
    wp_client._session = lambda: FakeSession()
    wp_client.list_categories = lambda: {1: 'News'}
    wp_client.list_all_tags = lambda: {f'Tag{i}': i for i in range(1, 9)}
    wp_client.get_post_content = lambda pid: '<p>contenu</p>'
    return wp_client

def run(label, total=13000, size=20, max_batches=900, doublons=()):
    wp = FakeWP(total=total, doublons_horodatage=doublons)
    wpc = make_env(wp)
    import fetch_batch; importlib.reload(fetch_batch)
    fetch_batch.wp_client = wpc
    fetch_batch.STATE_PATH = Path('/tmp/st.json')
    fetch_batch.BATCHES_DIR = Path('/tmp/batches')
    Path('/tmp/st.json').unlink(missing_ok=True)
    import shutil; shutil.rmtree('/tmp/batches', ignore_errors=True)
    Path('/tmp/batches').mkdir(parents=True, exist_ok=True)

    total_tagges = 0
    lots = 0
    lots_vides = 0
    import io, contextlib
    for i in range(max_batches):
        sys.argv = ['x', '--size', str(size)]
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            fetch_batch.main()
        out = buf.getvalue()
        st = json.loads(Path('/tmp/st.json').read_text())
        queued = st.get('queued', [])
        if not queued:
            lots_vides += 1
            if 'Fin du catalogue' in out:
                break
            if lots_vides > 30:
                print('  !! trop de lots vides consécutifs -> blocage'); break
            continue
        lots_vides = 0
        for pid in queued:
            wp.tag(pid)
        total_tagges += len(queued)
        st['processed'] = st.get('processed', []) + queued
        st['queued'] = []
        Path('/tmp/st.json').write_text(json.dumps(st))
        lots += 1

    restants = wp.nb_sans_tags()
    print(f"{label}")
    print(f"   articles taggés : {total_tagges}/{total}   lots : {lots}   restants : {restants}")
    print(f"   requêtes API totales : {wp.requests}  (moyenne {wp.requests/max(lots,1):.1f}/lot)")
    verdict = "OK - catalogue entier traité" if restants == 0 else f"INCOMPLET ({restants} non traités)"
    print(f"   -> {verdict}\n")
    return restants

print("=== TEST A : catalogue complet de 13000 articles, lots de 20 ===")
r1 = run("A", total=13000, size=20)

print("=== TEST B : horodatages en double (import en masse) ===")
r2 = run("B", total=500, size=20, doublons=(120, 121, 122, 300, 301))

print("=== TEST C : petit catalogue, vérif fin propre ===")
r3 = run("C", total=45, size=20)

print("RESULTAT GLOBAL :", "TOUS OK" if r1 == r2 == r3 == 0 else "ECHEC")