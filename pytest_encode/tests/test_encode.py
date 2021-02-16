# -- coding: utf-8 --
# @ModuleName:test_encode.py
# @Author:wanwan
# @Time:2021/2/14 16:00
import pytest

@pytest.mark.parametrize('name',['测试', '卡卡卡'])
def test_encode(name):
    print(name)