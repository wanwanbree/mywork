# -- coding: utf-8 --
# @ModuleName:test
# @Author:wanwan
# @Time:2021/1/30 10:28

from fun.calculation import Calulation
import pytest
import sys
from util.yaml_control import YamlControl

sys.path.append(".")

@pytest.fixture()
def login():
    print("测试登录")

def test_01(login):
    pass


def test_02():
    pass


class TestWork:

    #获取数据
    yamlcon = YamlControl()
    datas_add = yamlcon.readyaml("add.yml")
    # datas_div = yamlcon.readyaml("division.yml")
    # datas_mul = yamlcon.readyaml("multiplication.yml"

    @pytest.mark.parametrize("a, b, c", datas_add["add"]["datas"], ids=datas_add["add"]["ids"])
    def test_add(self,get_cal, a, b, c):
        assert c == get_cal.myadd(a, b)

    @pytest.mark.parametrize("a, b, c", datas_add["div"]["datas"], ids=datas_add["div"]["ids"])
    def test_devision(self,get_cal, a, b, c):
        #@pytest.raises()
        assert c == get_cal.division(a, b)

    @pytest.mark.parametrize("a,b,c", datas_add["mul"]["datas"], ids=datas_add["mul"]["ids"])
    def test_mul(self, get_cal,a, b, c):
        assert c == get_cal.multiplication(a, b)
