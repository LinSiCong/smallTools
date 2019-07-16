#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/3/23 
# @Time    : 10:32
# @Author  : LinSicong
# @File    : edgeDetection.py

import cv2



def laplacian(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
    gray_lap = cv2.Laplacian(image_gray, cv2.CV_16S, ksize=3)
    return cv2.convertScaleAbs(gray_lap)
