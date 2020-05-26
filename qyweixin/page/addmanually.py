from random import randint

from selenium.webdriver.common.by import By
from qyweixin.public.base import PageBase


class Addmanually(PageBase):
    """手动添加详细页"""
    def inputname(self,name):
        #输入姓名
        self.send_keys(By.XPATH,"//*[contains(@text,'姓名')]/..//*[@resource-id='com.tencent.wework:id/au7']",name)
        return self
    def choicesex(self):
        #选择性别
        self.click(By.XPATH,"//*[@resource-id='com.tencent.wework:id/dvl']")
        self.click(By.XPATH, "//*[@text='女']")
        return self

    def inputemail(self,email):
        #填写邮箱
        self.send_keys(By.XPATH,"//*[contains(@text,'邮箱')]/..//*[@resource-id='com.tencent.wework:id/au7']",email)
        return self
    def choiceaddress(self):
        #地址填写
        self.click(By.XPATH, "//*[contains(@text,'地址')]/..//*[@resource-id='com.tencent.wework:id/av9']")
        return Address(self._driver)
    def choiceidentity(self):
        #身份选择
        self.click(By.XPATH,"//*[@text='普通成员']")
        return Identity(self._driver)
    def add_manually(self):
        #保存
        self.click(By.XPATH,"//*[@text='保存']")
        from qyweixin.page.addmember import Addmember
        return Addmember(self._driver)

class Address(PageBase):
    def choiceaddress(self,address):
        #选择地址
        self.send_keys(By.XPATH,'//*[@resource-id="com.tencent.wework:id/h1"]',address)
        self.click(By.XPATH,"//*[@text='确定']")
        return Addmanually(self._driver)
class Identity(PageBase):
    def identity(self):
        i=randint(0,1)
        if i==1:
            self.click(By.XPATH, "//*[@text='普通成员']")
            return Addmanually(self._driver)
        else:
            self.click(By.XPATH, "//*[@text='上级']")
            return Addmanually(self._driver)
