from typing import List

from jsonpath import jsonpath

from framework.http import Http
from model.goods_api import GoodsApi
from model.user_api import UserApi
from utils.log import log


class GoodsHttpApi(GoodsApi):
    def __init__(self, user_api: UserApi):
        super().__init__(user_api)

    def search(self, keyword: str, page=1, limit=10) -> List[int]:
        r = Http.request_http(
            path='/wx/goods/list',
            method='get',
            headers={'X-Litemall-Token': self.user_api.get_token()},
            query={
                'keyword': keyword,
                'page': page,
                'limit': limit
            },
            data={}
        )
        if jsonpath(r.json(), '$.errno')[0] == 0:
            goods_list = jsonpath(r.json(), '$..list..id')
            log.debug(goods_list)
            return goods_list
        else:
            return -1

    def detail(self, goods_id: int) -> int:
        r = Http.request_http(
            path='/wx/goods/detail',
            method='get',
            headers={'X-Litemall-Token': self.user_api.get_token()},
            query={'id': goods_id},
            data={}
        )
        if jsonpath(r.json(), '$.errno')[0] == 0:
            product_id = jsonpath(r.json(), '$..productList..id')[0]
            log.debug(product_id)
            return product_id
        else:
            return -1

    def add_in_cart(self, goods_id: int, number: int, product_id: int):
        r = Http.request_http(
            path='/wx/cart/add',
            method='post',
            headers={'X-Litemall-Token': self.user_api.get_token()},
            query={},
            data={
                'goodsId': goods_id,
                'number': number,
                'productId': product_id
            }
        )
