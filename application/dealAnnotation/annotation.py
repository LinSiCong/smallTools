#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/9/1 
# @Time    : 10:55
# @Author  : LinSicong
# @File    : annotation.py

from dealJson import JsonProcessor


class BoundingBox:

    def __init__(self, xmin=None, ymin=None, xmax=None, ymax=None):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def init(self, bndbox):
        self.xmin = bndbox[0]
        self.ymin = bndbox[1]
        self.xmax = bndbox[2]
        self.ymax = bndbox[3]

    @property
    def width(self):
        return self.xmax - self.xmin

    @property
    def height(self):
        return self.ymax - self.ymin

    @property
    def bndbox(self):
        return [self.xmin, self.ymin, self.xmax, self.ymax]

    def __str__(self):
        return "(xmin:{:.2f}, ymin:{:.2f}, xmax:{:.2f}, ymax:{:.2f})".format(self.xmin, self.ymin, self.xmax, self.ymax)


class Annatation:
    """
        用作保存VOC格式文件数据的类
    """

    def __init__(self):
        self.data = {}

    @property
    def Classes(self):
        return self.data.keys()

    @property
    def valueList(self, className):
        return self.data[className]

    def addClass(self, className):
        if className not in self.data:
            self.data[className] = []

    def addLabel(self, className, value):
        if className in self.data:
            self.data[className].append(value)
        else:
            self.data[className] = [value]

    def readFromXML(self, xml_path):
        pass

    def readFromJson(self, json_path):
        self.data = JsonProcessor.loadJsonFile(json_path)

    def writeToJson(self, json_path):
        JsonProcessor.writeJsonFile(self.data, json_path)


    def showData(self):
        for key in self.data:
            print(key)
            for val in self.data[key]:
                pass


if __name__ == '__main__':
    pass
