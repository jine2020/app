from requests_wework.api.base_api import BaseApi


class WeWork(BaseApi):

    def get_token(self,secret):
        _corpid = 'ww7c598bbdd3aa6f03'
        _corpsecret = secret
        data={
            'method':'get',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params':{
                'corpid': _corpid,
                'corpsecret': _corpsecret
            }
        }

        return self.send(**data)['access_token']
