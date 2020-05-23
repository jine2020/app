import yaml
import pytest
from appium.webdriver.common.mobileby import MobileBy

from xueqiutask.page import Add_optional
from xueqiutask.equals import Equal


class TestAddOptional(Add_optional,Equal):
    """检查搜索股票后加自选"""

    @pytest.mark.parametrize('keys,StockNo', yaml.safe_load(open('./date.yml', encoding='utf-8'))['data'])
    @pytest.mark.parametrize('type1', yaml.safe_load(open('./date.yml', encoding='utf-8'))['type1'])
    @pytest.mark.parametrize('toast', yaml.safe_load(open('./date.yml', encoding='utf-8'))['toast'])
    @pytest.mark.parametrize('errortext', yaml.safe_load(open('./date.yml', encoding='utf-8'))['toasterrortext'])
    def test_add_optional(self, keys, StockNo, type1,toast,errortext):
        """测试加自选按钮"""
        data1, data2 = self.add_optional(keys, StockNo)
        text = self.find_toast_text(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        #断言 button toast
        self.equal(data1, data2, type1,errortext)
        self.equaltoast(data1,type1,toast,text,errortext)


if __name__ == '__main__':
    pytest.main(["-vs"])
