from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from seleniumhub.test_case.xueqiutask.base import Base


class Add_optional(Base):
    def add_optional(self, keys, StockNo):
        self.click(MobileBy.XPATH,"//*[@text='行情']")
        self.click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.send_keys(keys, MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        self.click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name']")
        locctor2 = (MobileBy.XPATH,
            f"//*[@text='{StockNo}']/../../../android.widget.LinearLayout[3]/android.widget.TextView")
        textstart = self.get_attribute_text(*locctor2)
        self.click(*locctor2)
        textend = self.get_attribute_text(*locctor2)
        return textstart, textend
