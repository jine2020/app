from appium import webdriver

from framework.common.base import Base
from framework.page.main import Main


class App(Base):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        # 启动app
        if self._driver==None:
            des = {
                "platformName": "android",
                "deviceName": '127.0.0.1:7555',
                "appPackage": self._package,
                "appActivity": self._activity,
                "noReset": True,
                "unicodeKeyBord": "true",
                "resetKeyBord": "true",
                "automationName": "uiautomator2"
            }
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        # 重启app
        pass

    def stop(self):
        # 关闭app
        pass
    def go_back(self):
        from framework.page.result import Result
        Result(self._driver).goto_main()
    def main(self) -> Main:
        return Main(self._driver)