import json
from dataclasses import dataclass, field, asdict

import requests

from utils.data import Data
from utils.log import log


class Http:
    """
    封装requests，实现通用的http处理，也为将来替换requests提供了便捷
    """

    @staticmethod
    def request_http(path, method, headers, query, data):
        request = Request()
        request.path = path
        request.method = method
        request.headers = headers
        request.query = query
        request.data = data

        r = request.send()
        return r


@dataclass
class Request:
    method: str = None
    host: str = None
    path: str = None
    query: dict = None
    '''
    如果通过调用 field() 指定字段的默认值，则该字段的类属性将替换为指定的 default 值。如果没有提供 default ，那么将删除类属性。
    目的是在 dataclass() 装饰器运行之后，类属性将包含字段的默认值，就像指定了默认值一样。
    ·default_factory ：如果提供，它必须是一个零参数可调用对象，当该字段需要一个默认值时，它将被调用。
     除了其他目的之外，这可以用于指定具有可变默认值的字段，如下所述。同时指定 default 和 default_factory 将产生错误。
    '''
    # headers: dict = field(default_factory=dict)
    headers: dict = None
    type: str = "json"
    data: dict = None

    def send(self):
        # 实现requests库的便捷封装或者替换

        # 多套环境
        env = Data.load_yaml('data/env.yaml')
        self.host = env[env['default']]

        # token处理
        # self.headers['token'] = token

        raw = None

        if self.type == 'json':
            self.headers['Content-Type'] = 'application/json'
            if self.data is None:
                raw = None
            else:
                raw = json.dumps(self.data)
        elif self.type == 'form':
            # 数据格式处理
            ...
        else:
            raise Exception("not exist format" + self.type)

        request_response = requests.request(
            method=self.method,
            url=self.host + self.path,
            params=self.query,
            headers=self.headers,
            data=raw,
            auth=None,
            verify=False
        )

        r = Response(request_response)
        log.debug(r.json())
        return r


@dataclass
class Response:

    def __init__(self, request_response: requests.Response):
        self.r = request_response

    def json(self):
        return self.r.json()

    @property
    def text(self):
        return self.r.text

    @property
    def status_code(self):
        return self.r.status_code
