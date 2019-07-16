#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/5/10 
# @Time    : 16:08
# @Author  : LinSicong
# @File    : test.py


import cv2

if __name__ == '__main__':
    img_path = "../testspace/label/0001.jpg"
    img = cv2.imread(img_path)
    print(type(img))
    cv2.imshow('test',img)
    cv2.waitKey(0)
    cv2.destroyWindow('test')

