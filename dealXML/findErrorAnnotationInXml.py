#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/10/5 
# @Time    : 1:11
# @Author  : LinSicong
# @File    : findErrorAnnotationInXml.py


import glob
from xml.dom import minidom

rootPath = "D:\Data\pigdata\data\\train\Annotations"
xmlList = glob.glob(rootPath + "/*.xml")
annotationList = ('pig', 'head', 'tail')

for xmlName in xmlList:

    dom = minidom.parse(xmlName)
    rootNode = dom.documentElement
    objectNodes = rootNode.getElementsByTagName('object')
    for objectNode in objectNodes:
        name = (objectNode.getElementsByTagName('name'))[0].firstChild.data
        flag = False
        for annontation in annotationList:
            if name == annontation:
                flag = True
        if not flag:
            print(name + "              " + xmlName)

print("done!")

