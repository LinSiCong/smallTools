#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/22 
# @Time    : 20:05
# @Author  : LinSicong
# @File    : renameSomeFile.py

from dealFile import dealFile
import os

if __name__ == '__main__':
    path = "D:\Data\pigBack\source"
    for dir in os.listdir(path):
        if dir != "010":
            continue
        subPath = os.path.join(path, dir)
        if os.path.isdir(subPath):
            for sdir in os.listdir(subPath):
                ssubPath = os.path.join(subPath, sdir)
                print(ssubPath)
                if os.path.isdir(ssubPath):
                    dealFile.renameAllFile(os.path.join(subPath, sdir), prefix=dir + "_" + sdir + "_")

