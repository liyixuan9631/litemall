from api.http.cart_http_api import CartHttpApi
from model.cart_api import CartApi
from model.user_api import UserApi


class CartApiFactory:
    @classmethod
    def create(cls, automation, user_api: UserApi):
        if automation == 'http':
            return CartHttpApi(user_api)
        elif automation == 'xml':
            ...
        elif automation == 'rpc':
            ...
        else:
            return CartApi(user_api)