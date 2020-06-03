from testframework.common.base import Base


class Result(Base):

    def add_optional(self,StockNo):
        #点击加自选
        self._params = {}
        self._params["StockNo"]=StockNo
        self.steps('../data/result.yml')
        return self

    def get_text(self,StockNo):
        #获取按钮文本，
        self._params = {}
        self._params["StockNo"]=StockNo
        return self.steps('../data/result.yml')


    def get_toast_text(self):
        #获取toast文本
        return  self.steps('../data/result.yml')

    def goto_main(self):
        self.steps('../data/result.yml')

        from testframework.page.main import Main
        return Main(self._driver)
