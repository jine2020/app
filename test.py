import os
import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestAutoLogin():
    '''测试微信cookie自动登录并点击通讯录'''
    def setup_method(self):
        if os.path.exists(os.path.dirname(r'cookies.dat')):
            pass
        else:
            try:
                os.remove(r'cookies.bak')
                os.remove(r'cookies.dat')
                os.remove(r'cookies.dir')
            except:
                pass
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open('cookies')
        db['cookie'] = self.driver.get_cookies()

        self.driver=webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

    def teardown_method(self):
        self.driver.quit()

    def test_AutoLogin(self):
        #通过cookie自动登录
        db=shelve.open('cookies')
        cookies=db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        #点击通讯录
        self.driver.find_element(By.ID,'menu_contacts').click()
        sleep(3)
