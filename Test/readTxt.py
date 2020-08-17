#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/3/1 
# @Time    : 16:13
# @Author  : LinSicong
# @File    : readTxt.py

import numpy as np
from dealString import StringProcessor

if __name__ == '__main__':
    path = "D:\Data\pigPose\Inception_v3 train data.txt"

    strLs = np.loadtxt(path, delimiter="\n", dtype=type("str"))
    for str in strLs:
        numLs = StringProcessor.readNums(str)
        if len(numLs) == 9:
            print(str)
            print(numLs)
