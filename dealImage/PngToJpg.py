#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/20 
# @Time    : 13:14
# @Author  : LinSicong
# @File    : PngToJpg.py
"""
将同目录下所有png文件保存为jpg文件
"""
import os
import cv2


if __name__ == '__main__':
    work_dir = os.getcwd()
    convert_dir = os.path.join(work_dir, "convertFile")
    if not os.path.exists(convert_dir):
        os.makedirs(convert_dir)
    file_list = os.listdir(work_dir)
    cot = 0
    for name in file_list:
        if os.path.splitext(name)[-1] == ".png":
            img = cv2.imread(os.path.join(work_dir, name))
            cv2.imwrite(os.path.join(convert_dir, name.replace(".png",".jpg")), img)
            cot = cot + 1
    print("Convert " + str(cot) + " images.")
