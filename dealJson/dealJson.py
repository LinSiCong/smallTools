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


