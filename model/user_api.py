from model.user_model import UserModel


class UserApi:

    def __init__(self, user: UserModel):
        self.user = user
        self._token = None

    # 注册
    def register(self):
        ...

    # 登陆
    def login(self):
        ...

    def set_token(self, token):
        self._token = token

    def get_token(self):
        return self._token
