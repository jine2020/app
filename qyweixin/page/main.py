from selenium.webdriver.common.by import By
from qyweixin.page.mainlist import Mainlist
from qyweixin.public.base import PageBase


class Main(PageBase):
    """消息页"""
    def news(self):
        #点击通讯录
        self.click(By.XPATH,'//*[@text="通讯录"]')
        return Mainlist(self._driver)