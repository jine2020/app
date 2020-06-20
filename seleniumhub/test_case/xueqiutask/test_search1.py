import sys
import yaml
import pytest
sys.path.append(r'C:\Users\lenovo\PycharmProjects\app')
from seleniumhub.test_case.xueqiutask.equals import Equal
from seleniumhub.test_case.xueqiutask.page import Add_optional


class TestAddOptional(Add_optional,Equal):
    """检查搜索股票后加自选"""

    @pytest.mark.parametrize('keys,StockNo', yaml.safe_load(open(r'C:\Users\lenovo\PycharmProjects\app\seleniumhub\test_case\xueqiutask/date.yml', encoding='utf-8'))['data'])
    @pytest.mark.parametrize('type1', yaml.safe_load(open(r'C:\Users\lenovo\PycharmProjects\app\seleniumhub\test_case\xueqiutask/date.yml', encoding='utf-8'))['type1'])
    @pytest.mark.parametrize('toast', yaml.safe_load(open(r'C:\Users\lenovo\PycharmProjects\app\seleniumhub\test_case\xueqiutask/date.yml', encoding='utf-8'))['toast'])
    @pytest.mark.parametrize('errortext', yaml.safe_load(open(r'C:\Users\lenovo\PycharmProjects\app\seleniumhub\test_case\xueqiutask/date.yml', encoding='utf-8'))['toasterrortext'])
    def test_add_optional1(self, keys, StockNo, type1,toast,errortext):
        """测试加自选按钮"""
        data1, data2 = self.add_optional(keys, StockNo)
        #断言 button
        self.equal(data1, data2, type1,errortext)


if __name__ == '__main__':
    pytest.main(["-vs"])
