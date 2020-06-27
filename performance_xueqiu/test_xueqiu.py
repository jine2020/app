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
#
# from time import sleep
#
# from appium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def test_xueqiu():
#     caps = {}
#     caps["platformName"] = "Android"
#     caps["deviceName"] = "127.0.0.1:7555"
#     caps["appPackage"] = "com.xueqiu.android"
#     caps["appActivity"] = ".view.WelcomeActivityAlias"
#     caps['noReset'] = "true"
#     caps['chromedriverExecutable']="D:/chromedriver/chromedriver233.exe"
#     driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
#     driver.implicitly_wait(15)
#     driver.find_element(By.XPATH, "//*[@text='交易']").click()
#     sleep(3)
#     webview = driver.contexts[-1]
#     driver.switch_to.context(webview)
#     performance = driver.execute_script("return window.performance.timing")
#     print(performance['domComplete'] - performance['responseStart'])

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


import subprocess
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By


def test_vmxueqiu():
    cmd="adb shell vmstat"
    res=subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(str(res.stdout.read(),encoding='GBK').split("\r\n")[2].split()[3])

class TestXueqiu(unittest.TestCase):
    def test_navigation(self):
        des = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": 'true',
            "chromedriverExecutable": 'D:\chromedriver\chromedriver223.exe'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
        self.driver.implicitly_wait(25)
        self.driver.find_element(By.XPATH,'//*[@text="交易"]').click()

        webview=self.driver.contexts[-1]
        self.driver.switch_to.context(webview)

        url=self.driver.execute_script("return window.location.href")
        print(url)


def test_draw():
    cmd="adb shell dumpsys gfxinfo com.xueqiu.android"
    res=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    lines=res.stdout.readlines()
    i=1
    for line in lines:
        i+=1
        if 'com.xueqiu.android.common.MainActivity' in line.decode('utf-8'):
            break
    lines =[x.decode('utf-8').replace("\r\n",'').replace('\t','').split() for x in lines]
    lines=lines[i:i+120]
    datas=[[] for row in range(4)]
    xx:str
    for xx in lines:
        datas[0].append(float(xx.split()[0]))
        datas[0].append(float(xx.split()[1]))
        datas[0].append(float(xx.split()[2]))
        datas[0].append(float(xx.split()[3]))
    #生成画布
    fig=pyplot.figure()
    #折线图
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.plot(datas[0])
    ax1.set_title('draw')
    #直方图
    ax1 = fig.add_subplot(2, 2, 2)
    ax1.hist(datas[1],range(5))
    ax1.set_title('prepare')
    #散点图
    ax1 = fig.add_subplot(2, 2, 3)
    ax1.scatter(range(120),datas[2])
    ax1.set_title('process')
    #虚线图
    ax1 = fig.add_subplot(2, 2, 4)
    ax1.plot(range(120),datas[3],'k--')
    ax1.set_title('execute')
    pyplot.show()


