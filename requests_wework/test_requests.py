import re

from filelock import FileLock

from requests_wework.auto_data import auto_name
import pytest
import requests


_name=auto_name()

def test_demo():
    r = requests.get('http://api.gethub.com/enents')
    print(r.json)

@pytest.fixture(scope='session')
def test_token():
    with FileLock('session.lock'):
        _corpid = 'ww7c598bbdd3aa6f03'
        _corpsecret = 'kPD0yEMpM6PhxMYY2h1HO-GXoLmxIa2FMvYdWSpmUqw'
        res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={_corpid}&corpsecret={_corpsecret}')
    return res.json()['access_token']


def test_get(userid,test_token):
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}')
    return res.json()


def test_create(userid,name,mobile,test_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}', json=data)
    return res.json()


def test_update(userid,name,mobile,test_token):
    data={
        "userid": userid,
        "name": name,
        "mobile": mobile
    }
    res=requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}',json=data)
    return res.json()

def test_delete(userid,test_token):
    res=requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}')
    return res.json()

def test_create_data():

    data=[("userid"+str(x),
               'zhangsan'+str(x),
               "138%08d"%x) for x in range(10)]
    return data

@pytest.mark.parametrize('userid,name,mobile',test_create_data())
def test_all(userid,name,mobile,test_token):
    try:
        assert 'created'==test_create(userid,name,mobile,test_token)['errmsg']
    except AssertionError as a:
        if 'mobile existed' in a.__str__():
            re_userid=re.findall("mobile existed:(.*)",a.__str__())[-1]
            assert 'deleted'==test_delete(re_userid,test_token)['errmsg']
            assert 60111 == test_get(re_userid,test_token)['errcode']
            assert 'created' == test_create(userid, name, mobile,test_token)['errmsg']
    assert name==test_get(userid,test_token)['name']
    assert 'updated'==test_update(userid,name+name,mobile,test_token)['errmsg']
    assert name+name == test_get(userid,test_token)['name']
    assert 'deleted'==test_delete(userid,test_token)['errmsg']
    assert 60111== test_get(userid,test_token)['errcode']
