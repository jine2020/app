import os

import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():
    # 无界面运行浏览器自动化demo
    def setup(self):
        try:
            using_headless=os.environ['using_headless']
        except KeyError:
            using_headless=None
            print('没有配置环境变量 using_headless,按照有界面方式运行浏览器')
        options=Options()
        if using_headless is not None and using_headless.lower()=='true':
            options.add_argument('--headless')
        self._driver = webdriver.Chrome(options=options)
        self._driver.get('https://www.baidu.com/s?wd=%E7%99%BE%E5%BA%A6&ie=utf-8&tn=78040160_5_pg&ch=12')

    def teardown(self):
        self._driver.quit()

    @pytest.mark.parametrize('value', ['百度', '顺丰', '京东', '淘宝'])
    def test_demo(self, value):
        text = self._driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').text
        assert '百度一下' in text, '分布式运行失败'
        self._driver.find_element_by_xpath('//*[@id="kw"]').clear()
        self._driver.find_element_by_xpath('//*[@id="kw"]').send_keys(value)
        self._driver.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3)

    @pytest.mark.parametrize('value', ['百度', '顺丰', '京东', '淘宝'])
    def test_demo1(self, value):
        text = self._driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').text
        assert '百度一下' in text, '分布式运行失败'
        self._driver.find_element_by_xpath('//*[@id="kw"]').clear()
        self._driver.find_element_by_xpath('//*[@id="kw"]').send_keys(value)
        self._driver.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3)


if __name__ == '__main__':
    pytest.main()