#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/10/2 
# @Time    : 15:57
# @Author  : LinSicong
# @File    : Rename.py

import os

if __name__ == '__main__':
    path = os.getcwd()
    count = 0
    for name in os.listdir(path):
        filePath = os.path.join(path, name)
        if os.path.isfile(filePath):
            if name != "Rename.py":
                os.rename(filePath, os.path.splitext(name)[0] + "_re" + os.path.splitext(name)[1])
                count = count + 1
    print("Rename " + str(count) + " files.")
