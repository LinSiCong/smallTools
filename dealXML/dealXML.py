#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/3/29 
# @Time    : 9:51
# @Author  : LinSicong
# @File    : dealXML.py

from xml.dom import minidom
from dealXML import fixXML
import glob
import os

def dealErrorCode(filePath, outcode='utf-8'):
    """
    处理编码错误
    xml.parsers.expat.ExpatError: not well-formed
    """
    with open(filePath, 'r') as f:
        data = f.read()
    with open(filePath, 'w', encoding=outcode) as f1:
        f1.write(data)
    return

def readXML(xmlPath, encoding='utf-8'):
    return minidom.parseString(minidom.parse(xmlPath).toxml(encoding))  # 打开xml文档

def writeXML(savePath, dom, fix=True, indent='', addindent='\t', newl='\n',encoding='utf-8'):
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
    if fix:
        minidom.Element.writexml = fixXML.fixed_writexml
    dom.writexml(file, indent=indent, addindent=addindent, newl=newl, encoding=encoding)
    file.close()
    print("Write " + savePath + " successfully")
    return

def findXMLLabel(dom, labelname):
    # assert isinstance(dom, minidom.Document)
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


def createTextLabel(dom, labelname, value):
    textLabel = dom.createElement(labelname)
    labelText = dom.createTextNode(value)
    textLabel.appendChild(labelText)
    return textLabel

def createLabel(dom, labelname, children):
    assert isinstance(children, list)
    label = dom.createElement(labelname)
    for child in children:
        label.appendChild(child)
    return label

def getOnlyLabel(dom, labelname):
    ls = findXMLLabel(dom, labelname)
    assert len(ls) == 1
    return ls[0]

def getOnlyValue(dom, labelname):
    return getOnlyLabel(dom, labelname).firstChild.data


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
