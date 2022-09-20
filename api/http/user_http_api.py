from dataclasses import asdict

from jsonpath import jsonpath

from framework.http import Http
from model.user_api import UserApi
from model.user_model import UserModel


class UserHttpApi(UserApi):
    def __init__(self, user: UserModel):
        super().__init__(user)

    def login(self) -> str:
        r = Http.request_http(
            path='/wx/auth/login',
            method='post',
            headers={},
            query={},
            data=asdict(self.user)
        )
        self.set_token(jsonpath(r.json(), '$..token')[0])

