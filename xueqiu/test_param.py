from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from hamcrest import assert_that, close_to
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch:
    def setup(self):
        des = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # "appActivity": ".common.MainActivity",
            "noReset": True,
            "dontStopAppOnReset":True,
            "sikpServerInstallation":True,
            "unicodeKeyBoard": True,#设置这个跟下面那个可以输入中文
            "resetKeyBoard": True
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
        self.driver.implicitly_wait(15)

    def teardown(self):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
        pass

    @pytest.mark.parametrize('keys,type,price',[
        ('alibaba','09988',200),
        ('xiaomi','01810',12)])
    def test_search(self,keys,type,price):
        """打开雪球
            点击搜索
            输入albb or xiaomi
            点击第一个搜索结果
            判断股票价格"""
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el3.send_keys(keys)
        el4=self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/name')
        el4.click()
        price_el =self.driver.find_element(MobileBy.XPATH,
            f"//*[@text='{type}']/../../..//*[ @ resource-id = 'com.xueqiu.android:id/current_price']")
        current_price=float(price_el.text)
        assert_that(current_price,close_to(price,price*0.1))