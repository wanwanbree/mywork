# -- coding: utf-8 --
# @ModuleName:dependency.py
# @Author:wanwan
# @Time:2021/2/1 23:08

import pytest

class TestClass():

    @pytest.mark.dependency(name='a')
    @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency(name='b')
    def test_b(self):
        pass

    @pytest.mark.dependency(name='c',depends=["a"])
    def test_c(self):
        pass

    @pytest.mark.dependency(name='d',depends=["b"])
    def test_d(self):
        pass

    @pytest.mark.dependency(depends=["b", "c"])
    def test_e(self):
        pass