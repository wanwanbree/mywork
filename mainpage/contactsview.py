# -- coding: utf-8 --
# @ModuleName:contactsview
# @Author:wanwan
# @Time:2021/3/2 0:00
from util.random_control import random_x,random_tel
from time import sleep

class ContactsView:
    def __init__(self,driver):
        self.driver =driver
    """
    添加成员
    """
    def add_member(self):
        #单击添加成员
       self.driver.find_elements_by_xpath('//a[contains(text(),"添加成员")]')[-1].click()
       #生成测试名开头的4位用户名
       name = '测试'+ random_x(2)
        #填写用户名
       self.driver.find_element_by_id('username').send_keys(name)
        #填写5位数字字母组成的随机账号
       self.driver.find_element_by_id('memberAdd_acctid').send_keys(random_x(5))
        #填写随机生成的电话号码
       self.driver.find_element_by_id('memberAdd_phone').send_keys(random_tel())
        #单击保存并继续填写
       self.driver.find_elements_by_xpath('//a[contains(@class,"js_btn_continue")]')[0].click()
       return name

    """
    搜索成员名称
    keys:搜索词
    """
    def searchmember(self,keys):
        #搜索框输入收拾词
        self.driver.find_element_by_id('memberSearchInput').send_keys(keys)
        sleep(2)
        #如果搜索成功页面显示’成员详情‘字符，返回检测到’成员详情‘元素的总数
        return len(self.driver.find_elements_by_xpath('//span[contains(text(),"成员详情")]'))

