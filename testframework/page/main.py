from testframework.common.base import Base
from testframework.page.quotation import Quotation
from testframework.page.search import Search


class Main(Base):
    def search(self):
        #点击搜索
        self.steps('../data/main.yml','search')
        return Search(self._driver)
    def goto_quotation(self):
        #点击进入行情页
        self.steps('../data/main.yml','goto_quotation')
        return Quotation(self._driver)