#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/5/10 
# @Time    : 16:08
# @Author  : LinSicong
# @File    : test.py


import cv2
import os

def dataOnImg(img, label, box, score=None, thickness=2, color=(0, 0, 255), fontColor=(0, 0, 255),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, fontThickness=1):
    tempImg = img.copy()
    p1 = (box[0], box[1])
    p2 = (box[2], box[3])
    cv2.putText(tempImg, "(x, y) : (" + str(box[0]) + ", " + str(box[1]) + ")", (0, img.shape[0] - 5), fontFace, fontScale, fontColor, fontThickness)
    return tempImg

jpg_name = [
    "0123.avi_81565_pig1.jpg",
    "0123.avi_81565_head1.jpg",
    "0123.avi_81565_back1.jpg",
    "0123.avi_81565_tail1.jpg"
]

dataLs = [
    [1716, 350, 2138, 813, 1.0],
    [1953, 352, 2120, 521, 0.99],
    [1940, 502, 2055, 629, 1.0],
    [1720, 633, 1890, 808, 0.98],
]

lableLs = [
    "pig",
    "head",
    "back",
    "tail"
]

if __name__ == '__main__':
    pass
    srcPath = "D:\PycharmProjects\smallTools\\testspace\img\pig"
    for i in range(4):
        img = cv2.imread(os.path.join(srcPath, jpg_name[i]))
        cv2.imshow(lableLs[i], dataOnImg(img, lableLs[i], dataLs[i]))
    cv2.waitKey()


