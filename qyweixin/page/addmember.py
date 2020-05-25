from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from qyweixin.page.addmanually import Addmanually
from qyweixin.public.base import PageBase


class Addmember(PageBase):
    """添加成员页"""
    def add_member(self):
        #点击手动输入添加
        self.click(By.XPATH,"//*[contains(@text,'手动输入')]")
        return Addmanually(self._driver)
    def toast_text(self):
        #获取toast文本
        text=self.get_toast_text(MobileBy.XPATH,'//*[@class="android.widget.Toast"]')
        return text
    def go_back(self):
        #返回通讯录页
        self.click(By.XPATH,'//*[@resource-id="com.tencent.wework:id/gv3"]')
        from qyweixin.page.mainlist import Mainlist
        return Mainlist(self._driver)