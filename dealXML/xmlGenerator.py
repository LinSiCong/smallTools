#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/18 
# @Time    : 9:49
# @Author  : LinSicong
# @File    : xmlGenerator.py

from xml.dom import minidom
import os

class XMLGenerator:
    """
    XMLGenerator用于生成xml文档树，AnnotationGenerator用于生成特定结构的标签文档
    """
    def __init__(self):
        self.document = minidom.Document()

    def makeRootLabel(self, label):
        assert isinstance(label, minidom.Element)
        self.document.appendChild(label)

    def getDom(self):
        return self.document

    def generateLeafNode(self, labelName, text):
        """
        生成叶子节点（文本节点）
        :param labelName:   标签名
        :param text:    标签文本
        :return:    叶子节点
        """
        label = self.document.createElement(labelName)
        labelText = self.document.createTextNode(text)
        label.appendChild(labelText)
        return label

    def generateLabel(self, labelName, childLabelList):
        """
        生成标签树
        :param labelName: 标签名
        :param childLabelList: 子标签列表
        :return: 新标签
        """
        label = self.document.createElement(labelName)
        for childLabel in childLabelList:
            label.appendChild(childLabel)
        return label

    def writeXML(self, filePath):
        """
        写xml文件
        :param filePath:
        :return:
        """
        dirs = os.path.dirname(filePath)
        if not os.path.exists(dirs):
            os.makedirs(dirs)
            print(dirs + "is created")
        file = open(filePath, 'w')
        self.document.writexml(file, addindent='\t', newl='\n')
        file.close()
        # print("Write " + filePath + " successfully")


# 该类已弃用
# class AnnotationGenerator(XMLGenerator):
#     def __init__(self):
#         super(AnnotationGenerator, self).__init__()
#         self.labelList = []
#         self.objectLabelList = []
#
#     def generateObjectLabel(self, name, bndbox):
#         """
#         生成Object标签
#         :param name: 检测标签的名字
#         :param bndbox: 标签标签的区域，一个四元组（xmin, ymin, xmax, ymax）
#         :return: NULL
#         """
#         bndboxNode = [self.generateLeafNode("xmin", str(bndbox[0])),
#                       self.generateLeafNode("ymin", str(bndbox[1])),
#                       self.generateLeafNode("xmax", str(bndbox[2])),
#                       self.generateLeafNode("ymax", str(bndbox[3]))]
#         objectNode = [self.generateLeafNode("name", name),
#                       self.generateLeafNode("pose", "Unspecified"),
#                       self.generateLeafNode("difficult", str(0)),
#                       self.generateLeafNode("truncated", str(0)),
#                       self.generateLabel("bndbox", bndboxNode)]
#         self.objectLabelList.append(self.generateLabel("object", objectNode))
#
#     def generateAnnotationLabel(self, folderName, fileName, size):
#         """
#         生成annotation标签树
#         :param folderName: 文件夹名
#         :param fileName:  文件名
#         :param size:  图片尺寸，一个三元组（width， height，depth）
#         :return: 一个annotation标签树
#         """
#         self.labelList.append(self.generateLeafNode("folder", folderName))
#         self.labelList.append(self.generateLeafNode("filename", fileName))
#
#         sourceNode = [self.generateLeafNode("database", "My database"),
#                       self.generateLeafNode("annotation", "VOC2007"),
#                       self.generateLeafNode("image", "flickr"),
#                       self.generateLeafNode("flickrid", "NULL")]
#         self.labelList.append(self.generateLabel("source", sourceNode))
#
#         ownerNode = [self.generateLeafNode("flickrid", "NULL"),
#                      self.generateLeafNode("name", "SCAU640")]
#         self.labelList.append(self.generateLabel("owner", ownerNode))
#         sizeNode = [self.generateLeafNode("width", str(size[0])),
#                     self.generateLeafNode("height", str(size[1])),
#                     self.generateLeafNode("depth", str(size[2]))]
#         self.labelList.append(self.generateLabel("size", sizeNode))
#         self.labelList.append(self.generateLeafNode("segmented", str(0)))
#         self.labelList.extend(self.objectLabelList)
#         self.document.appendChild(self.generateLabel("annotation", self.labelList))








