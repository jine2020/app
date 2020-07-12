from unittest import TestCase

from interface import demo
class TestApiRequest(TestCase):
    req_data={
            "method": 'get',
            "url":'http://127.0.0.1:8088/demo.txt',
            'headers': None,
            'encoding': 'base64'
        }
    def test_send(self):
        ar=demo.ApiRequest()
        print(ar.send(self.req_data))