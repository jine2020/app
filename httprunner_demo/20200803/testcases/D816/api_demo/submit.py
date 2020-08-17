from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCaseSubmitd(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""
    _config=Config("submit")
    _conf=_config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf)

    teststeps = [
        Step(
            RunRequest("/api/login/submit")
                .with_variables(
                **{"length": "47", "referer": "https://${host}/login/password"}
            )
                .post("https://${host}/api/login/submit")
                .with_headers(**{"Content-Type": "${ContentType}", }, **_headers_post)
                .with_data(
                {"phone": "13544871706", "password": "100100", "remember": "true"}
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", None)
        ),]
if __name__ == '__main__':
    TestCaseSubmitd().test_start()