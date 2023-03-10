from rule34Py import rule34Py
import random


class Rule:
    def __init__(self):
        self.api = rule34Py()

    async def random_post(self, tags: list[str]) -> str or None:
        if len(tags) < 1:
            return self.api.random_post().image

        if len(tags) > 2:
            return self.api.random_post(tags=random.choices(tags, k=2)).image

        return self.api.random_post(tags=tags).image
