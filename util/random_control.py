# -- coding: utf-8 --
# @ModuleName:random_control.py
# @Author:wanwan
# @Time:2021/3/2 0:32

import random

def random_x(length):
    a = str()
    characters = 'qwertyuiopasdfghjklzxcvbnm' + '1234567890'
    for i in range(length):
        a =a + str(random.choice(characters))
    return a

def random_tel():
    a = '1'
    characters = '1234567890'
    for i in range(10):
        a =a + random.choice(characters)
    return a

print(random_x(3))