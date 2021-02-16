# -- coding: utf-8 --
# @ModuleName:yaml_control
# @Author:wanwan
# @Time:2021/1/31 11:26

import yaml
import os

class YamlControl:

    def readyaml(self,filename):
        path = os.path.abspath('..')
        yamlpath = os.path.join(path,'data',filename)
        with open(yamlpath,encoding='gbk') as f:
            yamldata = yaml.load(f.read())
            #print(yamldata)
            return yamldata

if __name__ == '__main__':
    yamlcon = YamlControl()
    print(yamlcon.readyaml('add.yml'))
