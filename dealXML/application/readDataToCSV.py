#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/11/17 
# @Time    : 19:32
# @Author  : LinSicong
# @File    : readDataToCSV.py

from dealXML import dealXML
from dealFile import FileProcessor
import os
import csv


def readData(xmlPath):
    store = []
    filename = os.path.basename(xmlPath)
    print(xmlPath)
    # print(xmlPath)
    dom = dealXML.readXML(xmlPath)
    for object in dealXML.findXMLLabel(dom, "object"):
        xcen = dealXML.getOnlyValue(object, "xcen")
        ycen = dealXML.getOnlyValue(object, 'ycen')
        store.append([filename, xcen, ycen])
    return store


def writeToCSV(csvPath, data):
    print(csvPath)
    f = open(csvPath, 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)


if __name__ == '__main__':
    dirPath = "D:\Data\Rice\labels\labels"
    csvPath = "D:\Data\Rice\labels\labels\\csv"
    if not os.path.isdir(csvPath):
        os.makedirs(csvPath)
    data = []
    for xml in os.listdir(dirPath):
        if FileProcessor.getExtName(xml) == 'xml':
            csvFile = os.path.join(csvPath, FileProcessor.getBaseName(xml) + ".csv")
            writeToCSV(csvFile, readData(os.path.join(dirPath, xml)))


