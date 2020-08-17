from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCaseLogin(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""
    _config=Config("login")
    _conf=_config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf)

    teststeps = [
        Step(
            RunRequest("/login")
                .with_variables(referer="https://${host}/", cookie='')
                .get("https://${host}/login")
                .with_headers(**_headers_get)
                .validate()
                .assert_equal("status_code", 200)
        ),]
if __name__ == '__main__':
    TestCaseLogin().test_start()