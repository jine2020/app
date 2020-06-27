import requests, pystache


class TestDemo():
    def test_get(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("https://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={'h': 'header demo'})
        print(r)
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == 'header demo'

    def test_json(self):
        r = requests.post('https://httpbin.testing-studio.com/post', json={'h': 'header demo'})
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['h'] == 'header demo'

    def test_mustache(self):
        print(pystache.render('Hi {{penson}}!',
                              {'penson': 'seveniruby'}))
