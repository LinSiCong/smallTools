#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/4 
# @Time    : 11:51
# @Author  : LinSicong
# @File    : handleXml.py

import glob
from xml.dom import minidom
from dealXML import dealXML



def handler(xmlpath):
    dom = minidom.parse(xmlpath)
    dealXML.setXMLLabel(dom, 'folder', 'spike')
    dealXML.setXMLLabel(dom, 'path', 'C:\\Users\\linking\\Desktop\\shuidao\\spike')

    f = open(xmlpath, 'w', encoding='utf-8')
    dealXML.writeXML(xmlpath,dom)
    f.close()

if __name__ == '__main__':
    rootPath = "D:\Data\Rice\spike2"
    xmlList = glob.glob(rootPath + "/*.xml")

    for xmlpath in xmlList:
        handler(xmlpath)
    print("done!")