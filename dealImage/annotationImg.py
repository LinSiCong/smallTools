#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/3 
# @Time    : 18:03
# @Author  : LinSicong
# @File    : annotationImg.py

import os
import cv2


def annotionOnImg(img, label, box, score, thickness=2, color=(0, 0, 255), isText=True, fontColor=(0, 0, 255),
                  fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, fontThickness=1):
    tempImg = img.copy()
    p1 = (box[0], box[1])
    p2 = (box[2], box[3])
    cv2.rectangle(tempImg, p1, p2, color, thickness)
    if isText:
        p3 = (box[0] + 5, box[3] - 5)
        cv2.putText(tempImg, label + " " + str(score), p3, fontFace, fontScale, fontColor, fontThickness)
    return tempImg
