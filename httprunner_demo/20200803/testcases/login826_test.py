import pytest
from httprunner import Parameters
from httprunner import HttpRunner, Config, Step, RunTestCase
from testcases.D816.api_demo.home import TestCaseHome as home
from testcases.D816.api_demo.login import TestCaseLogin as login
from testcases.D816.api_demo.password import TestCasePassword as password
from testcases.D816.api_demo.submit import TestCaseSubmitd as submit
from testcases.D816.api_demo.list import TestCaseList as list
from testcases.D816.api_demo.tip_new_update import TestCaseTip_new_update as tip_new_update
from testcases.D816.api_demo.get_message_unread import TestCaseGet_message_unread as get_message_unread
from testcases.D816.api_demo.list_get import TestCaseGet_list as list_get
from api.public_api import ApiData as api

class TestCaseLogin826(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""
    @pytest.mark.parametrize("param",
                             Parameters({
                                 "phone-password-code-msg":api().login_data('phone-password-code-msg')
                                     # [
                                     #     ["13544871706",'100100', 0, None],
                                     #     ["1","100100",5,"数据验证失败，请重新提交"],
                                     #     ["", "100100", 5, "数据验证失败，请重新提交"],
                                     #     ["13544871706", "", 5, "数据验证失败，请重新提交"],
                                     #     ["13544871706", "111", 5, "帐号或密码错误，请重新输入"]
                                     # ],
                             }))
    def test_start(self, param):
        super().test_start(param)
    _config=Config("login")
    _conf=_config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf).variables(**{"phone": "1","password":"1","code":1,"msg":"1"})

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
