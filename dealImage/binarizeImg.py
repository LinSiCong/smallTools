#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/21 
# @Time    : 17:31
# @Author  : LinSicong
# @File    : binarizeImg.py

import cv2
import os


def binarization(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
    return cv2.threshold(image_gray, 0, 255, cv2.THRESH_OTSU)[1]


if __name__ == '__main__':
    jpg_dir = os.getcwd()
    jpg_ls = os.listdir()
    convert_dir = os.path.join(jpg_dir, "grayImage")
    if not os.path.exists(convert_dir):
        os.makedirs(convert_dir)
    cot = 0
    for jpg_name in jpg_ls:
        jpg_path = os.path.join(jpg_dir, jpg_name)
        if os.path.splitext(jpg_name)[-1] == ".jpg":
            img = cv2.imread(jpg_path)
            cv2.imwrite(os.path.join(convert_dir, jpg_name), binarization(img))
            cot = cot + 1
    print("Output " + str(cot) + " gray images.")
