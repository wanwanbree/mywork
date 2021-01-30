# -- coding: utf-8 --
# @ModuleName:test
# @Author:wanwan
# @Time:2021/1/30 10:28

from fun.calculation import Calulation
import pytest

cal = Calulation()

@pytest.mark.parametrize('a, b, c',[(1,2,3),(1,2,4),['a',2,5]])
def test_add(a, b, c):
    assert c==cal.myadd(a,b)
@pytest.mark.parametrize('a, b, c',[(1,0,0),(2,1,2.0)])
def test_devision(a,b,c):
    assert c==cal.division(a,b)
@pytest.mark.parametrize('a,b,c',[(2,21,42),(0,2,0)])
def test_mul(a,b,c):
    assert c==cal.multiplication(a,b)





