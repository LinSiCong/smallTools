#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/10 
# @Time    : 12:50
# @Author  : LinSicong
# @File    : checkAnnotation.py

import os
import cv2
from xml.dom import minidom

anntationDir = "../../testspace/VOC2010/Annotations"
jpgDir = "../../testspace/VOC2010/JPEGImages"

if __name__ == '__main__':

    anntationLs = sorted(os.listdir(anntationDir))
    jpgLs = sorted(os.listdir(jpgDir))
    cot = 0
    for anntationFile in anntationLs:
        type = anntationFile[-4:]
        if type == ".xml":
            cot = cot + 1
            name = anntationFile[:-4]
            img = cv2.imread(os.path.join(jpgDir, name + ".jpg"))
            height = img.shape[0]
            width = img.shape[1]

            def judge(xmin, ymin, xmax, ymax):
                pro = list()
                flag = True
                if xmin >= xmax:
                    pro.append("xmin >= xmax")
                    flag = False
                if xmin < 0:
                    pro.append("xmin < 0")
                    flag = False
                if xmax >= width:
                    pro.append("xmax >= weight")
                    flag = False
                if ymin >= ymax:
                    pro.append("ymax >= ymin")
                    flag = False
                if ymin < 0:
                    pro.append("ymin < 0")
                    flag = False
                if ymax >= height:
                    pro.append("ymax >= height")
                    flag = False
                return flag, pro


            dom = minidom.parse(os.path.join(anntationDir, anntationFile))
            labelH = int(dom.getElementsByTagName('height')[0].firstChild.data)
            labelW = int(dom.getElementsByTagName('width')[0].firstChild.data)
            flip = False

            if labelH == width and labelW == height:
                flip = True
                dom.getElementsByTagName('height')[0].firstChild.data = height
                dom.getElementsByTagName('width')[0].firstChild.data = width
                for object in dom.getElementsByTagName('object'):
                    xmin = int(object.getElementsByTagName('xmin')[0].firstChild.data)
                    ymin = int(object.getElementsByTagName('ymin')[0].firstChild.data)
                    xmax = int(object.getElementsByTagName('xmax')[0].firstChild.data)
                    ymax = int(object.getElementsByTagName('ymax')[0].firstChild.data)
                    object.getElementsByTagName('xmin')[0].firstChild.data = labelH - 1 - ymax
                    object.getElementsByTagName('ymin')[0].firstChild.data = xmin
                    object.getElementsByTagName('xmax')[0].firstChild.data = labelH - 1 - ymin
                    object.getElementsByTagName('ymax')[0].firstChild.data = xmax
                f = open(os.path.join(anntationDir, anntationFile), 'w', encoding='utf-8')
                dom.writexml(f, addindent='  ')
                f.close()
            ls = list()
            mp = dict()
            cnt = 0
            for object in dom.getElementsByTagName('object'):
                cnt += 1
                name = object.getElementsByTagName('name')[0].firstChild.data
                xmin = int(object.getElementsByTagName('xmin')[0].firstChild.data)
                ymin = int(object.getElementsByTagName('ymin')[0].firstChild.data)
                xmax = int(object.getElementsByTagName('xmax')[0].firstChild.data)
                ymax = int(object.getElementsByTagName('ymax')[0].firstChild.data)
                if xmin == 555 and ymin == 585 and xmax == 581 and ymax == 604:
                    print(anntationFile)
                flag, pro = judge(xmin, ymin, xmax, ymax)
                if not flag:
                    ls.append((cnt, name, pro))
            if flip or len(ls) > 0:
                print("------------------")
                print(anntationFile)
                print(width, width)
                print()
                print(len(ls))
                for t in ls:
                    print(t[0] , t[1], t[2])
                print("------------------")

