from string import Template

import yaml

from interface.qiyeweixin.api.base_api import BaseApi


class GetToken(BaseApi):

    def template(self,data1:list):
        with open('../api/get_token.yml') as f:
            data={
                "corpid" : data1[0],
                "corpsecret" : data1[1]
            }
            re=Template(f.read()).substitute(data)
            return yaml.safe_load(re)

    def get_token(self,data):
        req=self.template(data)
        r=self.requests_http(req)
        print(r.json())
        return r