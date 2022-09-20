from typing import List

from model.user_api import UserApi


class CartApi:
    def __init__(self, user_api: UserApi):
        self.user_api = user_api

    def list(self,) -> List[int]:
        ...
