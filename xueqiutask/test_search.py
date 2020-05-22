import yaml
import pytest
from xueqiutask.page import Add_optional
from xueqiutask.equals import equal


class TestAddOptional(Add_optional):
    """检查搜索股票后加自选"""

    @pytest.mark.parametrize('keys,StockNo', yaml.safe_load(open('./date.yml', encoding='utf-8'))['data'])
    @pytest.mark.parametrize('type1', yaml.safe_load(open('./date.yml', encoding='utf-8'))['type1'])
    def test_add_optional(self, keys, StockNo, type1):
        """测试加自选按钮"""
        data1, data2 = self.add_optional(keys, StockNo)
        equal(data1, data2, type1)


if __name__ == '__main__':
    pytest.main(["-vs"])
