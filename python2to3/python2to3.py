#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/5/1 
# @Time    : 0:08
# @Author  : LinSicong
# @File    : python2to3.py


import sys
from lib2to3.main import main

sys.exit(main("lib2to3.fixes"))

# 使用方法
# python python2to3.py -w 路径名