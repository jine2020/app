from appium import webdriver

from qyweixin.page.main import Main
from qyweixin.public.base import PageBase


class Start(PageBase):
    def start(self):
        if self._driver == None:
            des = {}
            des["platformName"] = "android"
            des["deviceName"] = "127.0.0.1:7555"
            des["appPackage"] = "com.tencent.wework"
            des["appActivity"] = ".launch.WwMainActivity"
            des["noReset"] = True
            des['dontStopAppOnReset'] = True
            des["uicodeKeyBord"] = "true"
            des["resetKeyBord"] = "true"
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def main(self) -> Main:
        return Main(self._driver)
    def go_back(self):
        from qyweixin.page.addmember import Addmember
        return Addmember(self._driver).go_back()

    def close(self):
        self._driver.quit()