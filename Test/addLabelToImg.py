#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/3 
# @Time    : 18:10
# @Author  : LinSicong
# @File    : addLabelToImg.py


import os
from application.dealAnnotation import annotationImg
import cv2

DATA_PATH = "../testspace/"


def readLabel(txt):
    m = {}
    for i in range(0, len(txt)):
        txt[i] = txt[i].split(' ')
        txt[i] = list(filter(None, txt[i]))
    txt = [x for x in txt if x != []]
    i = 0
    while i < len(txt):
        print(txt[i])
        label, num = txt[i]
        num = int(num)
        t = []
        for j in range(i + 1, i + num + 1):
            t.append(list(map(float, txt[j])))
        m[label] = t
        i = i + num + 1
    return m


if __name__ == '__main__':

    for i in [5, 9]:
        labelFile = "0" + str(i) + ".jpg.txt"
        imgFile = "0" + str(i) + ".jpg"
        txt = list()
        f = open(os.path.join(DATA_PATH, labelFile))

        txt = (f.read()).split("\n")
        label_map = readLabel(txt)
        img = cv2.imread(os.path.join(DATA_PATH, imgFile))
        print(type(img))
        print(label_map)
        for label in label_map:
            temp = img.copy()
            for data in label_map[label]:
                box = list(map(int, data[:4]))
                score = float('%.2f' % data[-1])
                temp = annotationImg.annotationOnImg(temp, label, box, score, thickness=3)
            cv2.imwrite(os.path.join(DATA_PATH, label + imgFile), temp)

        colorLs = [(0, 0, 255), (0, 255, 0), (0, 225, 255), (255, 255, 0), (255, 255, 255)]
        i = 0
        for label in label_map:
            for data in label_map[label]:
                box = list(map(int, data[:4]))
                score = data[-1]
                img = annotationImg.annotationOnImg(img, label, box, score, thickness=3, color=colorLs[i],
                                                    fontColor=colorLs[i])
            i = i + 1
        cv2.imwrite(os.path.join(DATA_PATH, "all" + imgFile), img)