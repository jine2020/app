import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import logging,time

logging.basicConfig(level=logging.INFO)
times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
def find_element(fuc):

    def find(*args,**kwargs):
        # 元素处理
        _black_list = {
            (By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, '//*[@text="确认"]'),
            (By.XPATH, '//*[@text="确定"]')
        }
        _max_num = 3
        _errort_num = 0
        selfs=args[0]
        try:
            logging.info(times+f' run {fuc.__name__}'+' args:'+repr(args[1:])+'\n'+repr(kwargs))
            fuc(*args, **kwargs)
            _errort_num = 0
            selfs._driver.implicitly_wait(3)
            return fuc(*args, **kwargs)
        except Exception as e:
            selfs.screenshort('../screenshort/tmp.png')
            with open("../screenshort/tmp.png",'rb') as f:
                content=f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            logging.error(times+' Not find element, enter blacklist processing!')
            selfs._driver.implicitly_wait(1)
            if _errort_num > _max_num:
                logging.error(times+' Not find element,blacklist processing failed!')
                raise e
            _errort_num += 1
            for element in _black_list:
                elelist = selfs._driver.find_elements(*element)
                if len(elelist) > 0:
                    elelist[0].click()
                    return fuc(*args, **kwargs)
            raise e
    return find

def waits(fuc):
    #显示等待
    def wait(*args,**kwargs):
        logging.info(times+f' run {fuc.__name__}' + ' args:' + repr(args[1:]) + '\n' + repr(kwargs))
        self=args[0]
        loc=args[1]
        ele=args[2]
        x=self._driver.find_elements(loc,ele)
        WebDriverWait(self._driver, 3).until(lambda s:len(x)>0)
        return fuc(*args,**kwargs)
    return wait
