from testframework.common.base import Base
from testframework.page.search import Search


class Quotation(Base):
    def goto_search(self):
        # self.steps('../data/quptation.yml')
        return Search(self._driver)