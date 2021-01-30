# -- coding: utf-8 --
# @ModuleName:test
# @Author:wanwan
# @Time:2021/1/30 10:28

from fun.calculation import Calulation
import pytest
import sys
sys.path.append('.')
def setup_module():
    print("每个模块内执行一次")

def teardown_module():
    print("每个模块内执行一次")

def setup_function():
    print("不在类内的每个用例内开始执行一次")

def teardown_function():
    print("不在类中的每个用例结束时执行")

def test_01():
    pass
def test_02():
    pass

class TestWork:

    def setup_class(self):
        print("类内执行一次开始")

    def teardown_class(self):
        print("类内执行一次结束")

    def setup_method(self):
        print("每个用例执行开始")

    def teardown_method(self):
        print("用例执行结束")

    def setup(self):
        print("每个用例执行一次")

    def teardown(self):
        print("每个用例结束执行")

    cal = Calulation()

    @pytest.mark.parametrize('a, b, c',[(1,2,3),(1,2,4),['a',2,5]])
    def test_add(self,a, b, c):
        assert c==self.cal.myadd(a,b)
    @pytest.mark.parametrize('a, b, c',[(1,0,0),(2,1,2.0)])
    def test_devision(self,a,b,c):
        assert c==self.cal.division(a,b)
    @pytest.mark.parametrize('a,b,c',[(2,21,42),(0,2,0)])
    def test_mul(self,a,b,c):
        assert c==self.cal.multiplication(a,b)

