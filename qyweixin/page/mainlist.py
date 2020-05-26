
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from qyweixin.page.addmember import Addmember
from qyweixin.page.information import Information
from qyweixin.public.base import PageBase


class Mainlist(PageBase):
    """通讯录页"""
    def mainlist(self):
        #点击添加成员
        self.click(By.XPATH,"//*[@text='添加成员']")
        return Addmember(self._driver)
    def findandclickmenber(self,name):
        #查询成员后点击
        self.click(By.XPATH,f'//*[@text="{name}"]')
        return Information(self._driver)

    def fiandmenber(self,name):
        try:
            self._driver.find_element_by_android_uiautomator(
                'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                'scrollIntoView(new UiSelector().text("{}").instance(0));'.format(name))
            return "False"
        except NoSuchElementException :
            return "True"
        except:
            return "False"


