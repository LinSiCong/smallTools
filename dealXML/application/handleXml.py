#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/4 
# @Time    : 11:51
# @Author  : LinSicong
# @File    : handleXml.py

import glob
from xml.dom import minidom

rootPath = "D:\Data\pigdata\data\\val\Annotations"
xmlList = glob.glob(rootPath + "/*.xml")

for xmlName in xmlList:
    dom = minidom.parse(xmlName)
    rootNode = dom.documentElement
    objectNodes = rootNode.getElementsByTagName('object')
    for objectNode in objectNodes:
        nameNode = objectNode.getElementsByTagName('name')
        if nameNode[0].firstChild.data == 'A':
            nameNode[0].firstChild.data = 'pig'
        elif nameNode[0].firstChild.data == 'B':
            nameNode[0].firstChild.data = 'pig'
        elif nameNode[0].firstChild.data == 'C':
            nameNode[0].firstChild.data = 'pig'
        elif nameNode[0].firstChild.data == 'D':
            # rootNode.removeChild(objectNode)
            nameNode[0].firstChild.data = 'pig'
    f = open(xmlName, 'w', encoding='utf-8')
    dom.writexml(f, addindent='  ')
    f.close()
print("done!")


