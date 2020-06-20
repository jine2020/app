import os
# sys.path.append(r'C:\Users\lenovo\PycharmProjects\app\seleniumhub\test_case')
from time import sleep
import pytest
from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
# from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestDW:
    def setup(self):
        des = {
            "platformName": "android",
            "deviceName": "MUMU",
            "udid":os.getenv("udid",None),
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            # "appActivity": ".common.MainActivity",
            "noReset": True,
            # "dontStopAppOnReset":True,
            # "unicodeKeyBoard": True,
            # "resetKeyBoard": True
        }
        # self.driver=webdriver.Remote('127.0.0.1:4723/wd/hub',des)
        self.driver = webdriver.Remote('192.168.109.1:4444/wd/hub', des)
        self.driver.implicitly_wait(15)
    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    @pytest.mark.parametrize('keys',['alibaba','xiaomi','腾讯','JD','BAIDU'])
    def test_search(self,keys):
        """打开雪球
            点击搜索
            输入albb or xiaomi
            点击第一个搜索结果
            判断股票价格"""
        sleep(2)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='行情']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.LinearLayout']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys(keys)
        sleep(5)
        # self.driver.find_element(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name']").click()



    # def test_alibaba(self):
    #     el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    #     print(el2.is_enabled())
    #     print(el2.text)
    #     print(el2.location)
    #     print(el2.size)
    #     el2.click()
    #     el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    #     el3.send_keys("alibaba")
    #     alibaba_element = self.driver.find_element_by_xpath(
    #         '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
    #     if alibaba_element.is_displayed() == True:
    #         print('搜索成功')
    #     else:
    #         print('搜索失败')
    #
    # def test_touchaction(self):
    #     sleep(10)
    #     action = TouchAction(self.driver)
    #     width = self.driver.get_window_rect()['width']
    #     height = self.driver.get_window_rect()['height']
    #     x = int(width / 2)
    #     y_start = int(height * 4 / 5)
    #     y_end = int(height * 1 / 5)
    #     action.press(x=x, y=y_start).wait(2000).move_to(x=x, y=y_end).release().perform()
    #     sleep(5)
    #     print("结束了")
    #
    # def test_albb(self):
    #     el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    #     el2.click()
    #     el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    #     el3.send_keys("阿里巴巴")
    #     el4 = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
    #     el4.click()
    #     print(self.driver.find_element_by_xpath(
    #         "//*[@text='09988']/../../..//*[ @ resource-id = 'com.xueqiu.android:id/current_price']").text)
    #     current_price = float(self.driver.find_element_by_xpath(
    #         "//*[@text='09988']/../../..//*[ @ resource-id = 'com.xueqiu.android:id/current_price']").text)
    #
    #     assert current_price > 200
    #
    # def test_loginxueqiu(self):
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
    #
    # def test_scroll_find_element(self):
    #     """滚动查找"""
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
    #     self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
    #                                                     'scrollIntoView(new UiSelector().text("今日话题").'
    #                                                     'instance(0));').click()
    #     sleep(5)
    #
    # def test_wait(self):
    #     el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    #     el2.click()
    #     el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    #     el3.send_keys("阿里巴巴")
    #     locctor=(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
    #     el4=WebDriverWait(self.driver,10).until(lambda x: x.find_element(*locctor))
    #     el4.click()
    #     current_price = float(self.driver.find_element_by_xpath(
    #         "//*[@text='09988']/../../..//*[ @ resource-id = 'com.xueqiu.android:id/current_price']").text)
    #     assert current_price > 200
    #
    # def test_network(self):
    #     #设置网络类型
    #     self.driver.set_network_connection(0)
    #     sleep(5)
    #     self.driver.set_network_connection(1)
    #     sleep(5)
    #     self.driver.set_network_connection(6)
    # def test_pho(self):
    #     #屏幕截图
    #     self.driver.get_screenshot_as_file("./pho/img.png")
    #     sleep(5)
    #     #录屏
    #     self.driver.start_recording_screen()
    #     self.driver.stop_recording_screen()

if __name__ == '__main__':
    pytest.main(['-vs'])
