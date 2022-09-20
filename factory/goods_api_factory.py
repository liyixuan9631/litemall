from api.http.goods_http_api import GoodsHttpApi
from model.goods_api import GoodsApi
from model.user_api import UserApi


class GoodsApiFactory:
    @classmethod
    def create(cls, automation, user_api: UserApi):
        if automation == 'http':
            return GoodsHttpApi(user_api)
        elif automation == 'xml':
            ...
        elif automation == 'rpc':
            ...
        else:
            return GoodsApi(user_api)