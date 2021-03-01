# -- coding: utf-8 --
# @ModuleName:test_wxaddmember
# @Author:wanwan
# @Time:2021/3/2 0:49

from mainpage.mainview import Mainview


def test_addmember():
    #添加成员
   name = Mainview().menu_contacts().add_member()
    #搜索新添加的成员
   assert Mainview().menu_contacts().searchmember(name) == 1