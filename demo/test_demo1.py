import time

import pytest
from time import sleep
from selenium import webdriver


class TestDemo():
    # 容器化ui自动化分布式demo
    def setup(self):
        # self._driver = webdriver.Remote('http://192.168.205.209:5001/wd/hub')
        self._driver = webdriver.Remote('http://192.168.43.76:5001/wd/hub')
        # self._driver=webdriver.Chrome()
        self._driver.get('http://192.168.43.161:1080/WebTours/')
        # self._driver.get('http://192.168.215.200:1080/WebTours/')
        # self._driver.save_screenshot('./jgp/shot'+str(time.localtime())+'.png')
        self._driver.implicitly_wait(10)

    def teardown(self):
        self._driver.quit()

    @pytest.mark.parametrize('adress',['xxx','xxx1','xxx2','xxx3'])
    def test_demo_webtours1(self,adress):
        self._driver.switch_to.frame(self._driver.find_element_by_name('body'))
        self._driver.switch_to.frame(self._driver.find_element_by_name('navbar'))
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td[2]/input').clear()
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td[2]/input').send_keys('jojo')
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[6]/td[2]/input').clear()
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[6]/td[2]/input').send_keys('bean')
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[9]/td[2]/input').click()
        sleep(1)
        self._driver.switch_to.default_content()
        self._driver.switch_to.frame(self._driver.find_element_by_name('body'))
        self._driver.switch_to.frame(self._driver.find_element_by_name('navbar'))
        self._driver.find_element_by_xpath('/html/body/center/center/a').click()
        sleep(1)
        self._driver.switch_to.default_content()
        self._driver.switch_to.frame(self._driver.find_element_by_name('body'))
        self._driver.switch_to.frame(self._driver.find_element_by_name('info'))
        select=self._driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[2]/td[2]/select')
        select.find_element_by_xpath('.//option[@value="London"]').click()
        self._driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[7]/td/input').click()
        self._driver.find_element_by_xpath('/html/body/blockquote/form/center/center/table/tbody/tr/td[1]/input').click()
        self._driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[8]/td[2]/input').clear()
        self._driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[8]/td[2]/input').send_keys(adress)
        self._driver.find_element_by_xpath('/html/body/blockquote/form/center/table/tbody/tr/td[1]/input').click()

    @pytest.mark.parametrize('adress',['xxx','xxx1','xxx2','xxx3'])
    def test_demo_webtours2(self,adress):
        self._driver.switch_to.frame(self._driver.find_element_by_name('body'))
        self._driver.switch_to.frame(self._driver.find_element_by_name('navbar'))
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td[2]/input').clear()
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[4]/td[2]/input').send_keys('jojo')
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[6]/td[2]/input').clear()
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[6]/td[2]/input').send_keys('bean')
        self._driver.find_element_by_xpath('/html/body/form/table/tbody/tr[9]/td[2]/input').click()
        sleep(1)
        self._driver.switch_to.default_content()
        self._driver.switch_to.frame(self._driver.find_element_by_name('body'))
        self._driver.switch_to.frame(self._driver.find_element_by_name('navbar'))
        self._driver.find_element_by_xpath('/html/body/center/center/a').click()
        sleep(1)
        self._driver.switch_to.default_content()
        self._driver.switch_to.frame(self._driver.find_element_by_name('body'))
        self._driver.switch_to.frame(self._driver.find_element_by_name('info'))
        select=self._driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[2]/td[2]/select')
        select.find_element_by_xpath('.//option[@value="London"]').click()
        self._driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[7]/td/input').click()
        self._driver.find_element_by_xpath('/html/body/blockquote/form/center/center/table/tbody/tr/td[1]/input').click()
        self._driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[8]/td[2]/input').clear()
        self._driver.find_element_by_xpath('/html/body/blockquote/form/table/tbody/tr[8]/td[2]/input').send_keys(adress)
        self._driver.find_element_by_xpath('/html/body/blockquote/form/center/table/tbody/tr/td[1]/input').click()
