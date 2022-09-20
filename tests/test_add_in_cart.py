from typing import List

from factory.cart_api_factory import CartApiFactory
from factory.goods_api_factory import GoodsApiFactory
from factory.user_api_factory import UserApiFactory
from model.user_api import UserApi
from model.user_model import UserModel
from utils.log import log


class TestAddInCart:
    def setup_class(self):
        user = UserModel()
        user.username = 'lyx'
        user.password = 'lyx123'
        self.user_api = UserApiFactory.create('http', user)
        self.user_api.login()

    def test_add_in_cart(self):
        goods_list = GoodsApiFactory.create('http', self.user_api).search('3D')
        if goods_list != -1:
            product_id = GoodsApiFactory.create('http', self.user_api).detail(goods_list[0])
            GoodsApiFactory.create('http', self.user_api).add_in_cart(goods_list[0], 1, product_id)
            goods_list_in_cart = CartApiFactory.create('http', self.user_api).list()
            assert goods_list[0] in goods_list_in_cart


