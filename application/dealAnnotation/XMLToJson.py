#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/26 
# @Time    : 16:14
# @Author  : LinSicong
# @File    : XMLToJson.py

from dealXML import dealXML
import json

def xmlToJson(xmlPath):
    dom = dealXML.readXML(xmlPath)
    objectLs = dealXML.findXMLLabel(dom, "object")

    return




if __name__ == '__main__':
    xmlPath = ""

    pass

