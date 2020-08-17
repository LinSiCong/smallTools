#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/17 
# @Time    : 17:27
# @Author  : LinSicong
# @File    : ImageProcessor.py

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

def cutImg(img, x, y, width, height):
    return img[x : x + width - 1, y :y + height - 1]

def cutImg(img, left_up, right_down):
    return img[left_up[0] : right_down[0], left_up[1] :right_down[1]]

if __name__ == '__main__':
    imgPath = ""
    for imgName in os.listdir(imgPath):
        if imgName[-4:] == ".jpg":
            img = cv2.imread(os.path.join(imgPath, imgName))
            img_h = horizontallyFlip(img)
            img_v = verticallyFlip(img)
