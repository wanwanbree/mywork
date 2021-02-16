# -- coding: utf-8 --
# @ModuleName:test_work2.py
# @Author:wanwan
# @Time:2021/1/31 15:01
import pytest
from fun.calculation import Calulation
from util.yaml_control import YamlControl


@pytest.fixture(params=['a','b'],ids=['case1','case2'])
def login(request):
    print("登录操作")
    return request.param

def test_search(login):
    print(login)
    print("搜索")




