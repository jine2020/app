# from appium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def test_xiuqiu():
#     des = {
#         "platformName": "android",
#         "deviceName": "127.0.0.1:7555",
#         "appPackage": "com.xueqiu.android",
#         "appActivity": ".view.WelcomeActivityAlias",
#         "noReset": True,
#         "chromedriverExecutable": 'D:\chromedriver\chromedriver223.exe'
#     }
#
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
#     driver.implicitly_wait(15)
#     driver.find_element(By.XPATH,'//*[@text="交易"]').click()
#     print(driver.page_source)
#     webview=driver.contexts[-1]
#     driver.switch_to.context(webview)
#     performance=driver.execute_script('return window.performance.timing')
#     print(performance)
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


def test_xueqiu():
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = "127.0.0.1:7555"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps['noReset'] = "true"
    caps['chromedriverExecutable']="D:/chromedriver/chromedriver233.exe"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, "//*[@text='交易']").click()
    sleep(3)
    webview = driver.contexts[-1]
    driver.switch_to.context(webview)
    performance = driver.execute_script("return window.performance.timing")
    print(performance['domComplete'] - performance['responseStart'])