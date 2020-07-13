import requests
from requests_wework.api.base_api import BaseApi
from requests_wework.api.wework import WeWork


class Address(BaseApi):
    def __init__(self):
        secret = 'kPD0yEMpM6PhxMYY2h1HO-GXoLmxIa2FMvYdWSpmUqw'
        self.get_token = WeWork().get_token(secret)

    def create(self, userid, name, mobile):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1]
        }
        res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token}', json=data)
        return res.json()

    def update(self, userid, name, mobile):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile
        }
        res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.get_token}', json=data)
        return res.json()

    def delete(self, userid):
        res = requests.get(
            f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token}&userid={userid}')
        return res.json()
