from selenium.webdriver.common.by import By

from qyweixin.page.editmember import Editmember
from qyweixin.public.base import PageBase


class Information(PageBase):
    def information(self):
        # 点击右上角图标
        self.click(By.XPATH, '//*[@resource-id="com.tencent.wework:id/gvd"]')
        return Editmember(self._driver)