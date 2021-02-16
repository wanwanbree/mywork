# -- coding: utf-8 --
# @ModuleName:test.py
# @Author:wanwan
# @Time:2021/1/30 23:00
import yaml
import pytest

yamlpath = "./data/add.yml"

with open(yamlpath) as f:
    yamldata = yaml.load(f.read(), Loader=yaml.FullLoader)
    print("dd:", yamldata)


@pytest.mark.parametrize("a,b,c", yamldata)
def test_01(a, b, c):
    assert c == a + b
