# -- coding: utf-8 --
# @ModuleName:test
# @Author:wanwan
# @Time:2021/1/3010:28
import logging

class Calulation:

    def myadd(self,a,b):
        try:
            c= a + b
            print(f"计算：{a}+{b}={c}")
            return c
        except Exception as e:
            logging.info()
            logging.info("计算异常:",e)

    def multiplication(self,a,b):
        try:
            c=a*b
            print(f"计算：{a}*{b}={c}")
            return c
        except Exception as e:
            logging.info("计算异常:",e)

    def division(self,a,b):
        try:
            c=a/b
            print(f"计算：{a}/{b}={c}")
            return c
        except Exception as e:
            print("计算异常:",e)


if __name__=="__main__":
    fun = Calulation()
    fun.add(1,2)
