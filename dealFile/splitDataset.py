#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/16 
# @Time    : 12:59
# @Author  : LinSicong
# @File    : splitDataset.py

import dealFile
import os

def generateNumList(total, rate):
    """
    生成切分数量列表，均匀分布，如将100分成6分生成[17,17,17,17,16,16]
    :param total: 总数
    :param rate: 切分份数
    :return: 列表
    """
    num = int(total / rate)
    r = total % rate
    L = []
    for x in range(0, rate):
        if x < r:
            L.append(num + 1)
        else:
            L.append(num)
    return L


def splitDataset(srcDir, dstDir, rate, newName="split", suffix=""):
    """
    遍历数据集，将数据集进行等比例切分
    :param srcDir:  数据集文件源目录
    :param dstDir:  分割后的数据集，存放的位置
    :param rate: 切分比例，切成几份
    :param newName: 分割后目录名
    :param suffix: 目录后缀，最后生成newName1/suffix
    :return:
    """
    files = os.listdir(srcDir)
    L = generateNumList(len(files), rate)
    cot = 0
    for i in range(0, len(L)):
        savePath = os.path.join(dstDir, newName + str(i + 1), suffix)
        if not os.path.exists(savePath):
            os.makedirs(savePath)
        T = L[i]
        while T:
            T -= 1
            dealFile.copyFile(os.path.join(srcDir, files[cot]), savePath)
            cot += 1
    print("Function splitDataset Done!"
          "Operate on" + str(cot) + "objects.")
    return

def copySameNameFile(fileDir, srcDir, dstDir, srcType, dstType):
    """
    一个目录下所有文件，对应另一个目录下同名但类型不同的文件，复制到指定目录
    主要用于数据处理是图片文件要与xml文件匹配的问题
    :param fileDir: 文件目录
    :param srcDir: 需要查找同名文件的目录
    :param dstDir: 目标目录
    :param srcType: 源文件类型
    :param dstType: 目标文件类型
    :return:
    """
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)
    cot = 0
    for filename in os.listdir(fileDir):
        if not dealFile.getExtName(filename) == srcType:
            continue
        srcFile = os.path.join(srcDir, dealFile.getBaseName(filename) + "." + dstType)
        dealFile.copyFile(srcFile, dstDir)
        cot += 1
    print("Function copySameNameFile Done! "
          "Operate on " + str(cot) + " objects.")
    return

def selectDatasetRandom(srcDir, dstDir, rate):
    """
    在数据中随机抽取
    :param srcDir: 数据集文件源目录
    :param dstDir: 抽取的得到的数据集
    :param rate: 抽取比例
    :return:
    """
    return

if __name__ == '__main__':
    # srcPath = "D:\Data\pigTrack\detect\JPEGImages"
    # dstPath = "D:\Data\pigTrack\detect\split"
    # splitDataset(srcPath, dstPath, 6, "detect", "JPEGImages")
    for i in range(0, 6):
        path1 = "D:\Data\pigTrack\detect\split\detect" + str(i+1) + "\JPEGImages"
        path2 = "D:\Data\pigTrack\detect\\xml"
        path3 = "D:\Data\pigTrack\detect\split\detect" + str(i+1) + "\Annotations"
        copySameNameFile(path1, path2, path3, "jpg", "xml")
