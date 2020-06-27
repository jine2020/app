import requests
from requests.auth import HTTPBasicAuth

def test_cookies():
    url='https://httpbin.testing-studio.com/cookies'
    header={
        'User-Agent':'hogwarts'
    }
    cookie_data={'hogwarts':'school',
                 'tearcher':'AD'}
    r=requests.get(url=url,headers=header,cookies=cookie_data)
    print(r.request.headers)

def test_oauth():
    r=requests.get(url='https://httpbin.testing-studio.com/basic-auth/banana/123',
                 auth=HTTPBasicAuth('banana','123'))
    print(r.text)