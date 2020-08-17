#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/3/29 
# @Time    : 17:11
# @Author  : LinSicong
# @File    : annotationProcessor.py

from dealXML import dealXML
from dealXML import xmlGenerator
from dealExcel import ExcelProcessor
import os
import cv2

def createAnnotation(labelTree):

    generator = xmlGenerator.XMLGenerator()

    def foo(labelMap):
        assert isinstance(labelMap, tuple) and len(labelMap) == 2
        key = labelMap[0]
        val = labelMap[1]
        if type(val) == list:
            labelLs = []
            for label in val:
                labelLs.append(foo(label))
            return generator.generateLabel(key, labelLs)
        else:
            return generator.generateLeafNode(key, str(val))

    generator.makeRootLabel(foo(labelTree))
    return generator

def generateLabelStruct(filename, jpgPath, width, height, depth):
    labelStruct = \
        ("annotation",[
            ("folder", "JPEGImages"),
            ("filename", filename),
            ("path", jpgPath),
            ("source", [
                ("database", "pigTrack")
                ]),
            ("size",[
                ("width", width),
                ("height", height),
                ("depth" , depth)
            ]),
            ("segmented" , "0")
        ])
    return labelStruct

def generateObjectNode(name, xmin, ymin, xmax, ymax):
    objectStruct = \
        ("object", [
            ("name", name),
            ("pose", "Unspecified"),
            ("truncated", "0"),
            ("difficult", "0"),
            ("bndbox",[
                ("xmin", xmin),
                ("ymin", ymin),
                ("xmax", xmax),
                ("ymax", ymax)
            ])
        ])
    return objectStruct


if __name__ == '__main__':
    xlsPath = "D:\PycharmProjects\smallTools\\testspace\label\\01.avi.xls"
    jpgPath = os.path.join(os.path.dirname(xlsPath), "1.jpg")
    img = cv2.imread(jpgPath)
    shape = img.shape
    row = ExcelProcessor.readData(xlsPath)[1][1]
    classes = ['A', 'B', 'C', 'D']

    labelTree = generateLabelStruct(os.path.basename(jpgPath), jpgPath, shape[0], shape[1], shape[2])
    for i in range(4):
       data = row[2 + i * 5 :  7 + i * 5]
       print(data)
       if float(data[4]) > 0:
           labelTree[1].append(generateObjectNode(classes[i], int(float(data[0])), int(float(data[1])), int(float(data[2])), int(float(data[3]))))
    print(labelTree)
    dom = createAnnotation(labelTree)
    dom.writeXML("D:\PycharmProjects\smallTools\\testspace\label\\1.xml")









