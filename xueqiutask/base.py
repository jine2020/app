from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    def setup_class(self):
        des = {
            "platformName": "android",
            "deviceName": '127.0.0.1:7555',
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "unicodeKeyBord": "true",
            "resetKeyBord": "true",
            "automationName":"uiautomator2"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
        self.driver.implicitly_wait(15)

    def setup(self):
        pass

    def teardown(self):
        self.click(MobileBy.XPATH, '//*[@text="取消"]')

    def teardown_class(self):
        self.driver.quit()

    def click(self, *parame):
        self.find_element(*parame).click()

    def send_keys(self, value, *parame):
        self.find_element(*parame).send_keys(value)

    def get_attribute_text(self, *parame):
        return self.find_element(*parame).get_attribute('text')
    def wait(self,parame,element):
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((parame,element)))
        return parame,element

    def find_element(self, *parame):
        ele = self.wait(*parame)
        return self.driver.find_element(*ele)
    def find_toast_text(self,parame,element):
        return self.driver.find_element(parame,element).text
