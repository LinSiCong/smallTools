#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/7 
# @Time    : 0:53
# @Author  : LinSicong
# @File    : JsonToXML.py

from dealJson import JsonProcessor
from dealXML import annotationProcessor
from batchProcessor.batchProcessor import batchProcessor

import os
import cv2


JsonDir = "D:\Data\pigTrack\detect\Json"

classes = ["A", "B", "C", "D", "head", "tail", "aback", "bback", "cback", "dback","back"]

def JsonToXML(jsonPath, xmlPath, imgPath):
    # imgPath = "D:\Data\pigTrack\detect\JPEGImages\\0123.avi_105298.jpg"
    # jsonPath = "D:\Data\pigTrack\detect\Json\\0123.avi_105298.json"
    # xmlPath = "D:\Data\pigTrack\detect\\xml\\0123.avi_105298.xml"

    json = JsonProcessor.loadJsonFile(jsonPath)
    img = cv2.imread(imgPath)
    shape = img.shape
    labelTree = annotationProcessor.generateLabelStruct(os.path.basename(imgPath), imgPath, shape[0], shape[1], shape[2])

    for cls in classes:
        for det in json[cls]["dets"]:
            labelTree[1].append(
                annotationProcessor.generateObjectNode(cls, det["xmin"], det["ymin"], det["xmax"], det["ymax"]))

    dom = annotationProcessor.createAnnotation(labelTree)
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

