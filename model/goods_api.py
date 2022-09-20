from typing import List

from model.user_api import UserApi


class GoodsApi:
    def __init__(self, user_api: UserApi):
        self.user_api = user_api

    def search(self, keyword: str, page=1, limit=10) -> List[int]:
        ...

    def detail(self, goods_id: int) -> int:
        ...

    def add_in_cart(self, goods_id: int, number: int, product_id: int):
        ...
