from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCaseList(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""
    _config=Config("list")
    _conf=_config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf)

    teststeps = [
        Step(
            RunRequest("/list")
                .with_variables(referer="https://${host}/login/password")
                .get("https://${host}/list")
                .with_headers(**_headers_get)
                .with_cookies(**_cookies)
                .validate()
                .assert_equal("status_code", 200)
        ),
        ]
if __name__ == '__main__':
    TestCaseList().test_start()