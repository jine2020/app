from framework.page.result import Result
from framework.common.base import Base


class Search(Base):
    def search(self,keys):
        #输入关键字选择第一个关联结果
        self._param={}
        self._param["keys"]=keys
        self.steps('../data/search.yml')
        return Result(self._driver)
