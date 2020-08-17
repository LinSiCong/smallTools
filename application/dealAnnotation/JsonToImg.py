#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/9/1 
# @Time    : 9:23
# @Author  : LinSicong
# @File    : JsonToImg.py


from dealImage import ImageProcessor
from dealJson import JsonProcessor


import cv2

JsonDir = "D:\Data\pigTrack\detect\Json"

classes = ["A", "B", "C", "D", "head", "tail", "aback", "bback", "cback", "dback","back"]

def JsonToImg(jsonPath, imgPath):
    # imgPath = "D:\Data\pigTrack\detect\JPEGImages\\0123.avi_105298.jpg"
    # jsonPath = "D:\Data\pigTrack\detect\Json\\0123.avi_105298.json"
    json = JsonProcessor.loadJsonFile(jsonPath)

    cv2.namedWindow("source")
    img = cv2.imread(imgPath)
    cv2.imshow("source", ImageProcessor.resize(img, 0.5))
    for cls in classes:
        for det in json[cls]["dets"]:
            drawBox(img, cls, det)

    cv2.namedWindow("new")
    cv2.imshow("new", ImageProcessor.resize(img, 0.5))

    cv2.waitKey(0)
    # 释放窗口
    cv2.destroyAllWindows()
    return

def drawBox(img, cls, det):
    p1 = (int(det["xmin"]), int(det["ymin"]))
    p2 = (int(det["xmax"]), int(det["ymax"]))
    cv2.rectangle(img, p1, p2, (0, 255, 0), 2, 1)
    p3 = (int(det["xmin"]) + 5, int(det["ymax"]) - 5)
    cv2.putText(img, cls + " " + str(det["score"]), p3, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    return

if __name__ == '__main__':
    JsonToImg("D:\Data\pigTrack\detect\Json\\0123.avi_105298.json", "D:\Data\pigTrack\detect\JPEGImages\\0123.avi_105298.jpg")