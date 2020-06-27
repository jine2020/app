import yaml
import pytest,sys
sys.path.append(r'C:\Users\lenovo\PycharmProjects\app')
from testframework.apps.appstart import App
from testframework.page.equals import Equal


class TestAddOptional(Equal):
    """检查搜索股票后加自选"""
    def setup_class(self):
        self.main = App()
        self.main.start()
    def setup(self):
        pass
    def teardown(self):
        self.main.go_back()
    def teardown_class(self):
        pass
    # @pytest.mark.skip
    @pytest.mark.parametrize('keys,StockNo', yaml.safe_load(open('../data/date.yml', encoding='utf-8'))['data'])
    @pytest.mark.parametrize('type1', yaml.safe_load(open('../data/date.yml', encoding='utf-8'))['type1'])
    @pytest.mark.parametrize('toast', yaml.safe_load(open('../data/date.yml', encoding='utf-8'))['toast'])
    def test_add_optional(self, keys, StockNo,toast, type1):
        """测试从主页下加自选"""
        data1=self.main.main().search().search(keys=keys).add_optional(StockNo=StockNo)
        data=data1.get_text(StockNo=StockNo)
        text=data1.get_toast_text()
        self.equal(data,type1)
        self.equaltoast(data, type1, toast, text)

    # @pytest.mark.skip
    @pytest.mark.parametrize('keys,StockNo', yaml.safe_load(open('../data/date.yml', encoding='utf-8'))['data'])
    @pytest.mark.parametrize('type1', yaml.safe_load(open('../data/date.yml', encoding='utf-8'))['type1'])
    @pytest.mark.parametrize('toast', yaml.safe_load(open('../data/date.yml', encoding='utf-8'))['toast'])
    def test_opthonnal_show(self,keys, StockNo,toast, type1):
        """测试从行情下加自选"""
        value=self.main.main().goto_quotation().goto_search().search(keys=keys).add_optional(StockNo=StockNo)
        data = value.get_text(StockNo=StockNo)
        text = value.get_toast_text()
        self.equal(data, type1)
        self.equaltoast(data, type1, toast, text)

