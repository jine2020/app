import pytest
from time import sleep
from selenium import webdriver


class TestDemo():
    # 容器化ui自动化分布式demo
    def setup(self):
        self._driver = webdriver.Remote('http://192.168.43.76:5001/wd/hub')
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