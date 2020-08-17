from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseCreate_doc(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""

    _config = Config("create_doc")
    _conf = _config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf)

    teststeps = [
        Step(
            RunRequest("/api/list/create_doc")
            .with_variables(**{"length": "17", "referer": "https://${host}/list"})
            .post("https://${host}/api/list/create_doc")
            .with_headers(**{"Content-Type": "${ContentType}",}, **_headers_post)
            .with_cookies(**_cookies)
            .with_data({"folderId": "0", "type": "0"})
            .extract()
            .with_jmespath("body.data.id", "id")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        )
    ]


if __name__ == "__main__":
    TestCaseCreate_doc().test_start()
