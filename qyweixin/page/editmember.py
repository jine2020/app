from selenium.webdriver.common.by import By

from qyweixin.page.edit import Edit
from qyweixin.public.base import PageBase


class Editmember(PageBase):
    def editmember(self):
        # 点击编辑成员按钮
        self.click(By.XPATH, '//*[@text="编辑成员"]')
        return Edit(self._driver)