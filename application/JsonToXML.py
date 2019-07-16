#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/7 
# @Time    : 0:53
# @Author  : LinSicong
# @File    : JsonToXML.py

from dealImage import dealImage
from dealJson import dealJson
from dealXML import dealXML
from dealXML import xmlGenerator
from dealXML import createAnnotation
from batchProcessor.batchProcessor import batchProcessor

import os
import cv2


JsonDir = "D:\Data\pigTrack\detect\Json"

classes = ["A", "B", "C", "D", "head", "tail", "aback", "bback", "cback", "dback","back"]

def JsonToImg(jsonPath, imgPath):
    # imgPath = "D:\Data\pigTrack\detect\JPEGImages\\0123.avi_105298.jpg"
    # jsonPath = "D:\Data\pigTrack\detect\Json\\0123.avi_105298.json"
    json = dealJson.loadJsonFile(jsonPath)

    cv2.namedWindow("source")
    img = cv2.imread(imgPath)
    cv2.imshow("source", dealImage.resize(img, 0.5))
    for cls in classes:
        for det in json[cls]["dets"]:
            drawBox(img, cls, det)

    cv2.namedWindow("new")
    cv2.imshow("new", dealImage.resize(img, 0.5))

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

def JsonToXML(jsonPath, xmlPath, imgPath):
    # imgPath = "D:\Data\pigTrack\detect\JPEGImages\\0123.avi_105298.jpg"
    # jsonPath = "D:\Data\pigTrack\detect\Json\\0123.avi_105298.json"
    # xmlPath = "D:\Data\pigTrack\detect\\xml\\0123.avi_105298.xml"

    json = dealJson.loadJsonFile(jsonPath)
    img = cv2.imread(imgPath)
    shape = img.shape
    labelTree = createAnnotation.generateLabelStruct(os.path.basename(imgPath), imgPath, shape[0], shape[1], shape[2])

    for cls in classes:
        for det in json[cls]["dets"]:
            labelTree[1].append(
                createAnnotation.generateObjectNode(cls, det["xmin"], det["ymin"],det["xmax"],det["ymax"]))

    dom = createAnnotation.createAnnotation(labelTree)
    dom.writeXML(xmlPath)
    return


def JsonToXMLProcessor(path, params):
    dir = os.path.join(os.path.dirname(path), "..")
    jsonName = os.path.basename(path)
    jsonPath = os.path.join(dir, "Json", jsonName)
    baseName = jsonName[:-(len(jsonName.split(".")[-1]) + 1)]
    imgName = baseName + ".jpg"
    imgPath = os.path.join(dir, "JPEGImages", imgName)
    xmlName = baseName + ".xml"
    xmlPath = os.path.join(dir, "xml", xmlName)
    JsonToXML(jsonPath, xmlPath, imgPath)
    return

if __name__ == '__main__':
    batchProcessor(JsonToXMLProcessor, [], JsonDir, "json")

