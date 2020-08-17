from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase



class TestCaseLogin826(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""
    _config=Config("login")
    _conf=_config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf)

    teststeps = [
        Step(
            RunRequest("/")
            .with_variables(referer='',cookie='')
            .get("https://${host}/")
            .with_headers(**_headers_get)
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login")
            .with_variables(referer="https://${host}/",cookie='')
            .get("https://${host}/login")
            .with_headers(**_headers_get)
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login/password")
            .with_variables(referer="https://${host}/login")
            .get("https://${host}/login/password")
            .with_headers(**_headers_get)
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/api/login/submit")
            .with_variables(
                **{"length": "47", "referer": "https://${host}/login/password"}
            )
            .post("https://${host}/api/login/submit")
            .with_headers(**{"Content-Type": "${ContentType}",}, **_headers_post)
            .with_data(
                {"phone": "13544871706", "password": "100100", "remember": "true"}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/list")
            .with_variables(referer="https://${host}/login/password")
            .get("https://${host}/list")
            .with_headers(**_headers_get)
            .with_cookies(**_cookies)
            .validate()
            .assert_equal("status_code", 200)
        ),
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
        Step(
            RunRequest("/api/message/get_message_unread")
            .with_variables(**{"length": "0", "referer": "https://${host}/list"})
            .post("https://${host}/api/message/get_message_unread")
            .with_headers(**_headers_post)
            .with_cookies(**_cookies)
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/api/list/get")
            .with_variables(**{"length": "38", "referer": "https://${host}/list"})
            .post("https://${host}/api/list/get")
            .with_headers(**{"Content-Type": "${ContentType}",}, **_headers_post)
            .with_cookies(**_cookies)
            .with_data({"folderId": "0", "sort": "time", "keywords": "", "source": ""})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
            .assert_equal("body.data.documents[0].name","欢迎使用幕布｜入门指南")
        ),
    ]


if __name__ == "__main__":
    TestCaseLogin826().test_start()
