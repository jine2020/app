import requests

_corpid = 'ww7c598bbdd3aa6f03'
_corpsecret = 'kPD0yEMpM6PhxMYY2h1HO-GXoLmxIa2FMvYdWSpmUqw'


def test_token():
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={_corpid}&corpsecret={_corpsecret}')
    print(res.json()['access_token'])
    return res.json()['access_token']

def test_get_department():
    res=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}&id=2')
    print(res.json())

def test_create_department():
    data={
        "name": "广州研发中心",
        "parentid": 1
    }
    res=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}',json=data)
    print(res.json())

def test_update_department():
    data={
        "id":2,
        "name": "测试学院"
    }
    res=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}',json=data)
    print(res.json())

def test_delete_department():
    res=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id=2')
    print(res.json())