#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/3/23 
# @Time    : 10:19
# @Author  : LinSicong
# @File    : duang.py

from dealImage import enhancetImg
from dealImage import binarizeImg
from dealImage import edgeDetection
import cv2

if __name__ == '__main__':
    imgPath = "D:\PycharmProjects\smallTools\\testspace\\20170301-11.jpg"
    savePath = "D:\PycharmProjects\smallTools\\testspace\\"
    img = cv2.imread(imgPath)
    cv2.imwrite(savePath + "binarize.jpg", binarizeImg.binarization(img))
    cv2.imwrite(savePath + "LaplaceEnhance.jpg", enhancetImg.LaplaceEnhance2(img))
    cv2.imwrite(savePath + "HistogramEqualization.jpg", enhancetImg.HistogramEqualization(img))
    cv2.imwrite(savePath + "edge.jpg", edgeDetection.laplacian(img))
