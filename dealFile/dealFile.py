#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/22 
# @Time    : 18:12
# @Author  : LinSicong
# @File    : dealFile.py


import os


def renameAllFile(path, prefix="", suffix=""):
    for name in os.listdir(path):
        filePath = os.path.join(path, name)
        if os.path.isfile(filePath):
            if name != "Rename.py":
                rename =  prefix + os.path.splitext(name)[0] + suffix + os.path.splitext(name)[1]
                os.rename(filePath,os.path.join(path, rename))
