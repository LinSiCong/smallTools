#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/2/28 
# @Time    : 1:22
# @Author  : LinSicong
# @File    : enhancetImg.py

import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import dealImage

def HistogramEqualization(img, other=[]):
    imgRGB = cv2.split(img)
    for i in range(3):
        cv2.equalizeHist(imgRGB[i], imgRGB[i])
    return cv2.merge(imgRGB)


def LaplaceEnhance(img, model=0):
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], np.float32)
    if model == 1:
        kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], np.float32)
    if model == 2:
        kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], np.float32)
    if model == 3:
        kernel = np.array([[-1, 1, -1], [1, 8, -1], [-1, 1, -1]], np.float32)
    return cv2.filter2D(img, -1, kernel)


def LaplaceEnhance2(img):
  kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #锐化
  return cv2.filter2D(img, -1, kernel=kernel)



if __name__ == '__main__':

    # srcPath = "D:/Data/Dataset/bee"

    srcPath = "D:\PycharmProjects\smallTools\\testspace\\20170301-11.jpg"
    srcImg = cv2.imread(srcPath)
    resizeRate = 0.3

    cv2.namedWindow("src")
    cv2.imshow("src", dealImage.resize(srcImg, resizeRate))



    # cv2.namedWindow("change")
    # cv2.imshow("change",dealImage.resize(LaplaceEnhance(srcImg), resizeRate))
    # cv2.namedWindow("change1")
    # cv2.imshow("change1", dealImage.resize(LaplaceEnhance(srcImg,1), resizeRate))
    # cv2.namedWindow("change2")
    # cv2.imshow("change2", dealImage.resize(LaplaceEnhance(srcImg,2), resizeRate))
    # cv2.namedWindow("change3")
    # cv2.imshow("change3", dealImage.resize(LaplaceEnhance(srcImg,3), resizeRate))
    cv2.namedWindow("change4")
    cv2.imshow("change4", dealImage.resize(LaplaceEnhance2(srcImg), resizeRate))
    cv2.namedWindow("change5")
    cv2.imshow("change5", dealImage.resize(HistogramEqualization(srcImg), resizeRate))


    cv2.waitKey(0)
    # 释放窗口
    cv2.destroyAllWindows()

