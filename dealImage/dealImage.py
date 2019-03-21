#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/17 
# @Time    : 17:27
# @Author  : LinSicong
# @File    : dealImage.py

import cv2
import numpy as np
import os

def resize(frame, rate):
    height = int(frame.shape[0] * rate)
    width = int(frame.shape[1] * rate)
    return cv2.resize(frame, (width, height))

def horizontallyFlip(frame):
    return cv2.flip(frame, 1)

def verticallyFlip(frame):
    return cv2.flip(frame, 0)

def rotate90(frame, rotate = 1):
    return np.rot90(frame, rotate)


if __name__ == '__main__':
    imgPath = ""
    for imgName in os.listdir(imgPath):
        if imgName[-4:] == ".jpg":
            img = cv2.imread(os.path.join(imgPath, imgName))
            img_h = horizontallyFlip(img)
            img_v = verticallyFlip(img)
