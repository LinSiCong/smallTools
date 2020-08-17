#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/11/25 
# @Time    : 20:12
# @Author  : LinSicong
# @File    : countLabels.py

from dealXML import dealXML
from dealFile import FileProcessor
import os
import csv


def countData(xmlPath, label):

    dom = dealXML.readXML(xmlPath)
    return len(dealXML.findXMLLabel(dom, label))


if __name__ == '__main__':
    dirPath = "D:\Data\Rice\labels\labels"
    mx = 0
    mxfile = ""
    mi = float("inf")
    data = []
    for xml in os.listdir(dirPath):
        if FileProcessor.getExtName(xml) == 'xml':
            size = countData(os.path.join(dirPath, xml), "object")
            if size > mx:
                mx = max(mx ,size)
                mxfile = xml
            if size < mi:
                mi = min(mi, size)
                mifile = xml
            if size > 40:
                data.append((size,xml))
    print(mx, mxfile)
    print(mi, mifile)
    for xml in data:
        print(xml)

