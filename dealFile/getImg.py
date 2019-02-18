#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/11/13 
# @Time    : 20:28
# @Author  : LinSicong
# @File    : getImg.py

import os
import shutil

if __name__ == '__main__':
    sourceDir = "D:\\Data\\Dataset\\testdata\\dataset"
    targetDir = "D:\Data\Dataset\\testdata\\traindata"
    file = open("D:\\Data\\Dataset\\testdata\\fileList.txt", "r")
    cot = 0
    while True:
        name = file.readline()

        if name != "":
            name = name.replace("\n", "") + ".jpg"
            targetFile = os.path.join(targetDir, name)
            sourceFile = os.path.join(sourceDir, name)
            shutil.copyfile(sourceFile, targetFile)
            cot = cot + 1
        else:
            break
    print("copy " + str(cot) + " images")
