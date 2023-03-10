from rule34Py import rule34Py
import random


class Rule:
    def __init__(self):
        self.api = rule34Py()

    async def random_post(self, tags: list[str]) -> str or None:
        if len(tags) < 1:
            post = self.api.random_post()

        elif len(tags) > 2:
            post = self.api.random_post(tags=random.choices(tags, k=2))

        else:
            post = self.api.random_post(tags=tags)

        if isinstance(post, list):
            return None
        return post.image

    async def search(self, tags: list[str] = (), limit: int = 10, page: int = 1) -> list[str] or None:
        if len(tags) < 1:
            posts = self.api.search(tags=tags, limit=limit, page_id=page)

        elif len(tags) > 2:
            posts = self.api.search(tags=random.choices(tags, k=2), limit=limit, page_id=page)
        else:
            posts = self.api.search(tags=tags, limit=limit, page_id=page)

        if len(posts) < 1:
            return None

        return list(map(lambda x: x.image, posts))
