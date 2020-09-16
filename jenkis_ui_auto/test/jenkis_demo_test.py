# encoding: utf-8
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():
    def setup(self):
        #namepath = os.path.abspath(os.path.dirname(__file__))
        #projectpath = namepath[:namepath.find("jenkis_ui_auto\\")] + "jenkis_ui_auto\\"
        path='/usr/local/tomcat/tomcat/webapps/chromedriver.exe'
        #try:
        #    using_headless=os.environ['using_headless']
        #except KeyError:
        #    using_headless=None
        #    print('no using_headless')
        options=Options()
        #if using_headless is not None and using_headless.lower()=='true':
        #    options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        self._driver = webdriver.Chrome(executable_path=path,options=options)
       
        self._driver.get('https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6&ie=utf-8&tn=78040160_5_pg&ch=12')

    def teardown(self):
        self._driver.quit()
        
    def test_demo(self, value='126'):
        text = self._driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').text
        self._driver.find_element_by_xpath('//*[@id="kw"]').clear()
        self._driver.find_element_by_xpath('//*[@id="kw"]').send_keys(value)
        self._driver.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3)

    def test_demo1(self, value='163'):
        text = self._driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').text
        self._driver.find_element_by_xpath('//*[@id="kw"]').clear()
        self._driver.find_element_by_xpath('//*[@id="kw"]').send_keys(value)
        self._driver.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3)


