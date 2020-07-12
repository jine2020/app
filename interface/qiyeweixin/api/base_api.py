import requests


class BaseApi:

    def requests_http(self,req):
        r=requests.request(**req)
        return r
