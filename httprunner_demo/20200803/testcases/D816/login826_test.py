from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.D816.api_demo.home import TestCaseHome as home
from testcases.D816.api_demo.login import TestCaseLogin as login
from testcases.D816.api_demo.password import TestCasePassword as password
from testcases.D816.api_demo.submit import TestCaseSubmitd as submit
from testcases.D816.api_demo.list import TestCaseList as list
from testcases.D816.api_demo.tip_new_update import TestCaseTip_new_update as tip_new_update
from testcases.D816.api_demo.get_message_unread import TestCaseGet_message_unread as get_message_unread
from testcases.D816.api_demo.list_get import TestCaseGet_list as list_get

class TestCaseLogin826(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""
    _config=Config("login")
    _conf=_config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf)

    teststeps = [
        Step(RunTestCase("home").call(home)),
        Step(RunTestCase("login").call(login)),
        Step(RunTestCase("password").call(password)),
        Step(RunTestCase("submit").call(submit)),
        Step(RunTestCase("list").call(list)),
        Step(RunTestCase("tip_new_update").call(tip_new_update)),
        Step(RunTestCase("get_message_unread").call(get_message_unread)),
        Step(RunTestCase("list_get").call(list_get)),

    ]


if __name__ == "__main__":
    TestCaseLogin826().test_start()
