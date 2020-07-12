import requests

class TestToken:
    corpid='ww7c598bbdd3aa6f03'
    corpsecret='kPD0yEMpM6PhxMYY2h1HO-GXoLmxIa2FMvYdWSpmUqw'
    def test_get_token(self):
        url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        params={
            'corpid':self.corpid,
            'corpsecret':self.corpsecret
        }
        r=requests.get(url=url,params=params)
        print(r.json())
        assert r.json()['errcode']==0