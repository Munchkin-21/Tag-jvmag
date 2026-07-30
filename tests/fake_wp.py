"""Faux WordPress : 13000 articles, gère before/page/per_page comme l'API réelle."""
from datetime import datetime, timedelta

BASE = datetime(2026, 6, 1, 12, 0, 0)

class FakeWP:
    def __init__(self, total=13000, doublons_horodatage=()):
        # article 0 = le plus récent. date décroissante d'1h par article.
        self.posts = []
        for i in range(total):
            d = BASE - timedelta(hours=i)
            self.posts.append({"id": 1000 + i, "date": d.isoformat(),
                               "title": {"rendered": f"Article {i}"},
                               "categories": [1], "tags": []})
        # forcer des horodatages identiques pour tester le cas des jumeaux
        for idx in doublons_horodatage:
            self.posts[idx]["date"] = self.posts[idx - 1]["date"]
        self.requests = 0

    def tag(self, post_id, n=8):
        for p in self.posts:
            if p["id"] == post_id:
                p["tags"] = list(range(1, n + 1))
                return

    def query(self, before=None, page=1, per_page=100):
        self.requests += 1
        sel = self.posts
        if before:
            cut = datetime.fromisoformat(before)
            sel = [p for p in sel if datetime.fromisoformat(p["date"]) < cut]
        start = (page - 1) * per_page
        return sel[start:start + per_page]

    def nb_sans_tags(self):
        return sum(1 for p in self.posts if len(p["tags"]) <= 1)