from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.D816.api_demo.create_doc import TestCaseCreate_doc as create_doc


class TestCaseDocid(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""

    _config = Config("docid")
    _conf = _config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf)

    teststeps = [
        Step(
            RunRequest("/doc${id}")
            .with_variables(**{"referer": "https://${host}/list"})
            .get("https://${host}/doc${id}")
            .with_headers(**_headers_get)
            .with_cookies(**_cookies)
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "text/html; charset=utf-8")
        )
    ]


if __name__ == "__main__":
    id=create_doc().test_start().with_export(['id'])
    TestCaseDocid().test_start()
