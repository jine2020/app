from selenium.webdriver.common.by import By
from qyweixin.public.base import PageBase


class Edit(PageBase):
    """编辑成员页"""
    def delmenber(self):
        #点击删除按钮
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                                         'scrollIntoView(new UiSelector().text("删除成员").instance(0));').click()
        self.click(By.XPATH,'//*[@text="确定"]')
        from qyweixin.page.mainlist import Mainlist
        return Mainlist(self._driver)

