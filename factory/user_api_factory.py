from api.http.user_http_api import UserHttpApi
from model.user_api import UserApi
from model.user_model import UserModel


class UserApiFactory:
    @classmethod
    def create(cls, automation, user: UserModel):
        if automation == 'http':
            return UserHttpApi(user)
        elif automation == 'xml':
            ...
        elif automation == 'rpc':
            ...
        else:
            return UserApi(user)
