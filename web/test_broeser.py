from time import sleep

from appium import webdriver


class TestBrower():
    def setup(self):
        des_caps={
            'platformName':'android',
            # 'platformVersion':'6.0',
            'browserName':'Browser',
            'noReset':True,
            'deviceName':'127.0.0.1:7555',
            # 'chromedriverExecutable':'D/chromedriver'

        }
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',des_caps)
        self.driver.implicitly_wait(15)
    def teardown(self):
        self.driver.quit()
    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        sleep(15)