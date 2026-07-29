"""Construit un lot d'articles sans tags à proposer pour tagging.

Usage: python scripts/fetch_batch.py --size 20
Écrit batches/batch_XXXX.json (XXXX = prochain numéro de lot disponible).
"""
import argparse
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

import wp_client

ROOT = Path(__file__).resolve().parent.parent
BATCHES_DIR = ROOT / "batches"
STATE_PATH = Path(__file__).resolve().parent / "state.json"


def load_state():
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text())
    else:
        state = {}
    state.setdefault("processed", [])
    state.setdefault("queued", [])
    state.setdefault("skipped", [])  # articles écartés (ex: encore en rédaction), à reconsidérer plus tard
    return state


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def next_batch_number():
    BATCHES_DIR.mkdir(exist_ok=True)
    existing = [p.stem for p in BATCHES_DIR.glob("batch_*.json") if "_proposed" not in p.stem and "_reviewed" not in p.stem]
    nums = [int(re.search(r"batch_(\d+)$", n).group(1)) for n in existing if re.search(r"batch_(\d+)$", n)]
    return (max(nums) + 1) if nums else 1


def html_to_text(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ")
    return re.sub(r"\s+", " ", text).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=20)
    args = parser.parse_args()

    state = load_state()
    skip_ids = set(state["processed"]) | set(state["queued"]) | set(state["skipped"])

    categories = wp_client.list_categories()
    all_tags_map = wp_client.list_all_tags()  # name -> id, snapshot live à l'instant du lot
    tags_by_id = {tid: name for name, tid in all_tags_map.items()}
    batch_posts = wp_client.list_untagged_posts(args.size, skip_ids=skip_ids)

    if not batch_posts:
        print("Aucun article sans tag restant à traiter (ou tous déjà en file).")
        return
    if len(batch_posts) < args.size:
        print(
            f"Note : seulement {len(batch_posts)}/{args.size} articles trouvés "
            "(limite de scan atteinte ou plus assez d'articles sans tag récents)."
        )

    articles = []
    for p in batch_posts:
        content_html = wp_client.get_post_content(p["id"])
        cat_names = [categories.get(cid, str(cid)) for cid in p.get("categories", [])]
        existing_tag_names = [tags_by_id.get(tid, str(tid)) for tid in p.get("tags", [])]
        articles.append(
            {
                "id": p["id"],
                "title": p["title"]["rendered"],
                "category": cat_names,
                "content_text": html_to_text(content_html),
                "existing_tags": existing_tag_names,
            }
        )

    batch_num = next_batch_number()
    out_path = BATCHES_DIR / f"batch_{batch_num:04d}.json"
    out_data = {
        "tags_existants": sorted(all_tags_map.keys()),
        "categories_existantes": sorted(categories.values()),
        "articles": articles,
    }
    out_path.write_text(json.dumps(out_data, indent=2, ensure_ascii=False))

    state["queued"].extend(p["id"] for p in batch_posts)
    save_state(state)

    print(f"Lot écrit : {out_path} ({len(articles)} articles)")


if __name__ == "__main__":
    main()
