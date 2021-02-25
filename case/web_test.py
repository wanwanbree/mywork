# -- coding: utf-8 --
# @ModuleName:web_test
# @Author:wanwan
# @Time:2021/2/25 20:55

from selenium import webdriver
import json
from time import sleep
import pytest

class TestTmp():

    def setup(self):
        #命令行启动 chrome -remote-debugging-port=9222
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address='127.0.0.1:9222'
        #self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip()
    def test_01(self):
        self.driver.get('https://work.weixin.qq.com')
        #self.driver.find_element_by_id('menu_contacts').click()
        cookies = self.driver.get_cookies()
        with open('tem_cookie.txt',mode='w',encoding='utf-8') as f:
            f.write(json.dumps(cookies))
        sleep(5)

    #@pytest.mark.skip()
    def test_02(self):
        self.driver.get('https://work.weixin.qq.com')
        with open('tem_cookie.txt',mode='r',encoding='utf-8') as f:
            [self.driver.add_cookie(i) for i in json.loads(f.read())]
        self.driver.find_element_by_class_name('index_top_operation_loginBtn').click()
        self.driver.find_element_by_id('menu_contacts').click()
        sleep(5)