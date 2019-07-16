#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/16 
# @Time    : 15:14
# @Author  : LinSicong
# @File    : dealJson.py


import json
import os

def loadJsonFile(file):
    if not os.path.exists(file):
        print(file + "is not exist")
        return dict()
    f = open(file, 'r')
    js = f.read()
    f.close()
    return json.loads(js)


def writeJsonFile(dic, file):
    dirs = os.path.dirname(file)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        print(dirs + "is created")
    f = open(file, 'w')
    f.write(json.dumps(dic))
    f.close()

if __name__ == '__main__':
    path = "../testspace"
    filename = "testJson.json"
    dic = {"a" : 12, "b" : "1000", "c" : "d"}
    writeJsonFile(dic, os.path.join(path, filename))
    dic = loadJsonFile(os.path.join(path, filename))
    print(dic)
