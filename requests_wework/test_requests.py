import requests

_corpid = 'ww7c598bbdd3aa6f03'
_corpsecret = 'kPD0yEMpM6PhxMYY2h1HO-GXoLmxIa2FMvYdWSpmUqw'


def test_demo():
    r = requests.get('http://api.gethub.com/enents')
    print(r.json)


def test_token():
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={_corpid}&corpsecret={_corpsecret}')
    print(res.json()['access_token'])
    return res.json()['access_token']


def test_get():
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token()}&userid=zhangsan')
    print(res.json())


def test_create():
    data = {
        "userid": "zhangsan",
        "name": "张三",
        "mobile": "13800000000",
        "department": [1]
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token()}', json=data)
    print(res.json())


def test_update():
    data={
        "userid": "zhangsan",
        "name": "李四",
        "mobile": "13800000999"
    }
    res=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token()}',json=data)
    print(res.json())

def test_delete():
    res=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token()}&userid=zhangsan')
    print(res.json())