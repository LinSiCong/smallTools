#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/22 
# @Time    : 18:12
# @Author  : LinSicong
# @File    : dealFile.py


import os
import shutil

def getBaseName(fileName):
    """
    获取文件名，去文件格式（后缀）
    :param fileName: 文件全名
    :return: 文件名
    """

    # tmp = fileName.split(".")
    # if len(tmp) > 1:
    #     return fileName[:-(len(tmp[-1])+1)]
    # return fileName
    pos = ("." + fileName).rindex(".")  # tip: rindex找不到会抛ValueError, 这里是个错误处理
    if pos > 0:
        return fileName[:pos-1]
    return fileName


def renameAllFile(path, prefix="", suffix="", mode=0, type="", startID=0, sort=False):
    """
    重命名目录下所有文件，命名方式：
    mode=0: 前缀 + 原名 + 后缀 + 文件格式
    mode=1: 前缀 + 编号（id） + 后缀 + 文件格式

    :param path: 文件目录
    :param prefix: 前缀
    :param suffix: 后缀
    :param mode: 重命名模式
    :param type: 文件格式，例如 .jpg
    :param sort: 是否排序
    :return:
    """
    cot = startID
    fileLs = os.listdir(path)
    if sort:
        fileLs.sort()
    for name in fileLs:
        filePath = os.path.join(path, name)
        if os.path.isfile(filePath):
            fileName = os.path.splitext(name)[0]
            fileType = os.path.splitext(name)[1]
            if type == "" or type == fileType:
                if mode == 1:
                    rename = prefix + str(cot) + suffix + fileType
                else:
                    rename =  prefix + fileName + suffix + fileType
                os.rename(filePath,os.path.join(path, rename))
                cot = cot + 1
    print("Rename " + str(cot) + " files in " + path)


def copyFile(srcFile, dstPath):
    if not os.path.isfile(srcFile):
        print(srcFile + " not exist.")
        return
    if os.path.normcase(os.path.dirname(srcFile)) == os.path.normcase(dstPath):
        print("Copying files in the same directory is not supported.")
        return
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    dstfile = os.path.join(dstPath, os.path.basename(srcFile))
    if os.path.isfile(dstfile):
        print("A file of the same name exists under the destination path.")
    shutil.copyfile(srcFile, dstfile)

def moveFile(srcFile, dstPath):
    if not os.path.isfile(srcFile):
        print(srcFile + " not exist.")
        return
    if os.path.normcase(os.path.dirname(srcFile)) == os.path.normcase(dstPath):
        print("Copying files in the same directory is not supported.")
        return
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    dstFile = os.path.join(dstPath, os.path.basename(srcFile))
    if os.path.isfile(dstFile):
        print("A file of the same name exists under the destination path.")
    shutil.move(srcFile, dstFile)

if __name__ == '__main__':
    srcFile = "testspace/img/05.jpg"
    dstPath = "testspace/img/copy"
