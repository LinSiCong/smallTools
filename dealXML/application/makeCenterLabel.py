#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/11/16 
# @Time    : 23:30
# @Author  : LinSicong
# @File    : makeCenterLabel.py

"""
    VOC2010格式数据标签，提取中心点，并保存中心点数据标签
"""

from xml.dom import minidom
from dealXML import dealXML
from batchProcessor.batchProcessor import batchProcessor

def makeCenterLabel(xmlPath, newPath = None):
    dom = dealXML.readXML(xmlPath)
    objectList = dealXML.findXMLLabel(dom, "object")
    for object in objectList:
        if len(dealXML.findXMLLabel(object, "center")) > 0:
            continue
        xmin = int(dealXML.getOnlyValue(object, "xmin"))
        xmax = int(dealXML.getOnlyValue(object, "xmax"))
        ymin = int(dealXML.getOnlyValue(object, "ymin"))
        ymax = int(dealXML.getOnlyValue(object, "ymax"))

        xcen = dealXML.createTextLabel(dom, "xcen", str(int((xmin + xmax) / 2)))
        ycen = dealXML.createTextLabel(dom, 'ycen', str(int((ymin + ymax) / 2)))
        object.appendChild(dealXML.createLabel(dom, "center", [xcen, ycen]))
    if newPath == None:
        newPath = xmlPath
    dealXML.writeXML(newPath, dom)

def centerlabelProcessor(path, params):
    makeCenterLabel(path)

if __name__ == '__main__':
    dirPath = "D:\Data\Rice\labels\labels"
    batchProcessor(centerlabelProcessor, "", dirPath, fileType="xml")
    # xmlPath = "D:\PycharmProjects\\smallTools\\testspace\label\\0001.xml"
    # newPath = "D:\PycharmProjects\\smallTools\\testspace\label\\0001test.xml"
    # makeCenterLabel(xmlPath, newPath)