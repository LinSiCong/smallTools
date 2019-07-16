#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/18 
# @Time    : 16:31
# @Author  : LinSicong
# @File    : generateAnnotation.py

from dealXML import xmlGenerator
import cv2
import os

"""
生成同目录下所有.jpg图片的统一标签，标定区域只有一个，标定区域大小为整个图片大小，root为图片
所在文件夹路径，默认是同目录下文件，label_name是标签名称，默认是pig
路径名不能包含中文，会报错。

"""

if __name__ == '__main__':
    root = os.getcwd()      #图片路径
    label_name = "pig"      #标签名称
    output_path = os.path.join(root, "Annotation")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    fileList = os.listdir(root)
    cot = 0
    for img_name in fileList:
        file_path = os.path.join(root, img_name)
        if os.path.isfile(file_path):
            if os.path.splitext(img_name)[-1] == ".jpg":
                img = cv2.imread(file_path)
                size = img.shape
                annotation = xmlGenerator.AnnotationGenerator()
                annotation.generateObjectLabel(img_name[-1], (1, 1, size[0], size[1]))
                annotation.generateAnnotationLabel(root, img_name, size)
                annotation.writeXML(os.path.join(output_path, os.path.splitext(img_name)[0] + ".xml"))
                cot = cot + 1
    print("Output " + str(cot) + " annotations.")