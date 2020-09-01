import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from httprunner import Parameters
from testcases.D816.api_demo.submit import TestCaseSubmitd as submit




class TestCaseSubmitd(HttpRunner):
    """使用如下功能需要修改testcase中标记为2020.08.17新增"""

    @pytest.mark.parametrize("param",
                             Parameters({
                                 "phone-password-code-msg":
                                     [
                                         ["13544871706",'100100', 0, None],
                                         ["1","100100",5,"数据验证失败，请重新提交"],
                                     ],
                             }))
    def test_start(self, param) :
        super().test_start(param)
    _config=Config("submit")
    _conf=_config.conf()
    _headers_get = _config.headers_get()
    _headers_post = _config.headers_post()
    _cookies = _config.cookies()

    config = _config.verify(False).variables(**_conf).variables(**{"phone": "1","password":"1","code":1,"msg":"1"})
    teststeps = [RunTestCase('submit').call(submit),]
if __name__ == '__main__':
    TestCaseSubmitd().test_start()