#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/6/17 
# @Time    : 8:37
# @Author  : LinSicong
# @File    : batchProcessor.py

import os

def batchProcessor(processor, params, dirPath, fileType=None):
    """
    批量处理器
    用于对一个目录下，同类型文件进行处理。
    使用时需要对要处理的函数再封装，封装的目的是进行参数解析。
    主要是一个扩展工具，使得原本对单个文件的处理，扩展到对一个目录下所有同类文件进行处理。
    :param processor: 高阶函数， 一般是无返回值的函数,需要自行再封装，做参数解析
    :param params: 参数列表
    :param dirPath: 文件目录
    :param fileType: 文件类型,不要带"."
    :return:
    """
    fileList = os.listdir(dirPath)
    if fileType != None:
        fileType = "." + fileType
        typeLen = len(fileType)
    for fileName in fileList:
        path = os.path.join(dirPath, fileName)
        if os.path.isfile(path):
            if fileType != None and (len(fileName) < typeLen or fileName[-typeLen:] != fileType):
                continue
            processor(path, params)

# demo
# 原函数
import cv2
import numpy as np


from tkinter import *
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

from skimage import data_dir,io,transform,color,filters

def Pic_Enhance(image):
    # 对比度增强############
    im = ImageEnhance.Contrast(image)
    im = im.enhance(1.1)
    # 图象冷暖色调整############
    r, g, b = im.split()
    r = r.point(lambda i: i * 1.1)
    g = g.point(lambda i: i * 0.9)
    b = b.point(lambda i: i * 0.9)
    im = Image.merge(im.mode, (r, g, b))

    # 图象增强############

    im = im.filter(ImageFilter.EDGE_ENHANCE)
    return im

# 由于原函数有返回值，在封装一层进行处理
def deal_img(img_path):
    image = Image.open(img_path)
    im = Pic_Enhance(image)
    # 后续处理
    im.save( "D:\PycharmProjects\smallTools\\testspace\save\\" + os.path.basename(img_path))
    return

# 对deal_img在封装一层，进行参数解析
def img_processor(path, params):
    deal_img(path)


if __name__ == '__main__':
    dirPath = "D:\PycharmProjects\smallTools\\testspace\img"
    batchProcessor(img_processor, "", dirPath, "jpg")
