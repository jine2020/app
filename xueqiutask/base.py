from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Base:
    def setup_class(self):
        des = {
            "platformName": "android",
            "deviceName": '127.0.0.1:7555',
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "unicodeKeyBord": "true",
            "resetKeyBord": "true"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
        self.driver.implicitly_wait(15)

    def setup(self):
        pass


    def teardown(self):
        self.click(MobileBy.XPATH, '//*[@text="取消"]')


    def teardown_class(self):
        self.driver.quit()

    def click(self,parame,element):
        self.driver.find_element(parame,element).click()
    def send_keys(self,value,*parame,):
        self.driver.find_element(*parame).send_keys(value)
    def get_attribute_text(self,*parame):
        return self.driver.find_element(*parame).get_attribute('text')