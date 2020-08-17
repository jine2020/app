from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCaseTip_new_update(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""
    _config=Config("tip_new_update")
    _conf=_config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf)

    teststeps = [
        Step(
            RunRequest("/api/list/tip_new_update")
                .with_variables(**{"length": "0", "referer": "https://${host}/list"})
                .post("https://${host}/api/list/tip_new_update")
                .with_headers(**_headers_post)
                .with_cookies(**_cookies)
                .with_data("")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", 0)
                .assert_equal("body.msg", None)
        ),
        ]
if __name__ == '__main__':
    TestCaseTip_new_update().test_start()