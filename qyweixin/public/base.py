from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class PageBase:
    _black_list = {
        (By.XPATH, '//*[@text="确认"]'),
        (By.XPATH, '//*[@text="确定"]')
    }
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value=None):
        #元素处理
        try:
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            self._errort_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._errort_num > self._max_num:
                raise e
            self._errort_num += 1
            for element in self._black_list:
                elelist = self._driver.find_elements(*element)
                if len(elelist) > 0:
                    elelist[0].click()
                    return self.find(locator, value)
            raise e

    def click(self,*loc):
        return self.find(*loc).click()

    def send_keys(self, loc, ele, text):
        return self.find(loc, ele).send_keys(text)

    def get_toast_text(self, *loc):
        return self.find(*loc).text


