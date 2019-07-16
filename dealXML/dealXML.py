#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/3/29 
# @Time    : 9:51
# @Author  : LinSicong
# @File    : dealXML.py

from xml.dom import minidom
import glob
import os

def readXML(xmlPath):
    return minidom.parse(xmlPath)   # 打开xml文档

def writeXML(savePath, dom):
    """
    写xml文件
    :param filePath:
    :return:
    """
    basePath = os.path.dirname(savePath)
    if not os.path.exists(basePath):
        os.makedirs(basePath)
    file = open(savePath, 'w')
    assert isinstance(dom, minidom.Document)
    dom.writexml(file, addindent='\t', newl='\n')
    file.close()
    print("Write " + savePath + " successfully")
    return

def findXMLLabel(dom, labelname):
    assert isinstance(dom, minidom.Document)
    return dom.getElementsByTagName(labelname)


def setXMLLabel(dom, labelname, val):
    labelLs = findXMLLabel(dom, labelname)
    for label in labelLs:
        txt = label.firstChild
        assert isinstance(txt, minidom.Text)
        txt.data = val

def modifyXMLLabel(dom, labelname, orign, val):
    labelLs = findXMLLabel(dom, labelname)
    for label in labelLs:
        txt = label.firstChild
        assert isinstance(txt, minidom.Text)
        if txt.data == orign:
            txt.data = val

if __name__ == '__main__':
    list = glob.glob("D:\Data\pigTrack\VOC2007\Annotations-src/*.xml")
    savePath = "D:\Data\pigTrack\VOC2007\Annotations"
    for path in list:
        dom = readXML(path)
        print(type(dom))
        modifyXMLLabel(dom, "name", "a", "aback")
        modifyXMLLabel(dom, "name", "b", "bback")
        modifyXMLLabel(dom, "name", "c", "cback")
        modifyXMLLabel(dom, "name", "d", "dback")
        writeXML(os.path.join(savePath,os.path.basename(path)), dom)
