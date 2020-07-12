from interface import test_demo1
class TestApi:
    data={
            "method": 'get',
            "url": 'http://testing-studio:8088/demo.txt',
            'headers': None,
        }
    def test_send(self):
        api=test_demo1.Api()
        print(api.send(self.data).text)

