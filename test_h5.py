from selenium import webdriver


class TestData:
    def test_data(self):
        #获取timing
        driver=webdriver.Chrome()
        driver.get('https://ceshiren.com/')
        print(driver.execute_script('return JSON.stringify(window.performance.timing)'))