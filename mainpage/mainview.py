# -- coding: utf-8 --
# @ModuleName:mainview
# @Author:wanwan
# @Time:2021/3/1 23:53
from selenium import webdriver

from mainpage.contactsview import ContactsView


class Mainview:
    def __init__(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def menu_contacts(self):
        self.driver.find_element_by_id('menu_contacts').click()
        return ContactsView(self.driver)
