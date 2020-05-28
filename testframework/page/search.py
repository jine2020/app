from testframework.page.result import Result
from testframework.common.base import Base


class Search(Base):
    def search(self,keys):
        #输入关键字选择第一个关联结果
        self._param={}
        self._param["keys"]=keys
        self.steps('../data/search.yml','search')
        return Result(self._driver)


if __name__ == '__main__':
    d={}
    d['keys']=3
    for key in d.keys():
        print(key)