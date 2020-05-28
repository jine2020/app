from selenium.webdriver.common.by import By

def find_element(fuc):
    def find(*keys,**kwargs):
        # 元素处理
        _black_list = {
            (By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, '//*[@text="确认"]'),
            (By.XPATH, '//*[@text="确定"]')
        }
        _max_num = 3
        _errort_num = 0
        selfs=keys[0]

        try:
            fuc(*keys, **kwargs)
            _errort_num = 0
            selfs._driver.implicitly_wait(10)
            return fuc(*keys, **kwargs)
        except Exception as e:
            selfs._driver.implicitly_wait(1)
            if _errort_num > _max_num:
                raise e
            _errort_num += 1
            for element in _black_list:
                elelist = selfs._driver.find_elements(*element)
                if len(elelist) > 0:
                    elelist[0].click()
                    return fuc(*keys, **kwargs)
            raise e
    return find