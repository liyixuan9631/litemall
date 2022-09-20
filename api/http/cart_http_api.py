from typing import List

from jsonpath import jsonpath

from framework.http import Http
from model.cart_api import CartApi
from model.user_api import UserApi


class CartHttpApi(CartApi):
    def __init__(self, user_api: UserApi):
        super().__init__(user_api)

    def list(self,) -> List[int]:
        r = Http.request_http(
            path='/wx/cart/index',
            method='get',
            headers={'X-Litemall-Token': self.user_api.get_token()},
            query={},
            data={}
        )

        if jsonpath(r.json(), '$.errno')[0] == 0:
            goods_list = jsonpath(r.json(), '$..cartList..goodsId')
            return goods_list
        else:
            return -1
