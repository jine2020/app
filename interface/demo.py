import requests,base64,json

class ApiRequest:
    def send(self,data:dict):
        res=requests.request(data['method'],data['url'],headers=data['headers'])
        if data['encoding']=='base64':
            return json.loads(base64.b64decode(res.content))
        elif data['encoding']=='base32':
            return json.loads(base64.b32decode(res.content))
        #把加密过后的响应值发给第三方服务，让第三方去做解密然后返回解密过后的信息
        elif data['encoding']=='private':
            return requests.post('url',data=res.content)