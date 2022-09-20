from dataclasses import dataclass


@dataclass
class UserModel:
    username: str = None
    password: str = None
