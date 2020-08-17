from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCaseGet_list(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""
    _config=Config("list_get")
    _conf=_config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf)

    teststeps = [
        Step(
            RunRequest("/api/list/get")
                .with_variables(**{"length": "38", "referer": "https://${host}/list"})
                .post("https://${host}/api/list/get")
                .with_headers(**{"Content-Type": "${ContentType}", }, **_headers_post)
                .with_cookies(**_cookies)
                .with_data({"folderId": "0", "sort": "time", "keywords": "", "source": ""})
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", None)
                .assert_equal("body.data.documents[0].name", "欢迎使用幕布｜入门指南")
        ),
        ]
if __name__ == '__main__':
    TestCaseGet_list().test_start()