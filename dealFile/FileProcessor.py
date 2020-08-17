#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/22 
# @Time    : 18:12
# @Author  : LinSicong
# @File    : FileProcessor.py


import os
import shutil

def listAllDirs(rootDir):
    """
    获取当前目录下所有目录
    :param rootDir:
    :return:
    """
    if(not os.path.isdir(rootDir)):
        return []
    dirLs = [rootDir]
    for dir in os.listdir(rootDir):
        currentPath = os.path.join(rootDir, dir)
        dirLs.extend(listAllDirs(currentPath))
    return dirLs

def listAllDirLeaves(rootDir):
    """
    获取当前目录下所有目录，叶子节点，不考虑文件
    :param rootDir:
    :return:
    """
    dirLs = []
    flag = False    # 标记是否有子目录
    for dir in os.listdir(rootDir):
        currentPath = os.path.join(rootDir, dir)
        if os.path.isdir(currentPath):
            dirLs.extend(listAllDirLeaves(currentPath))
            flag = True
    if not flag:
        dirLs.append(rootDir)
    return dirLs

def listAllFiles(rootDir, addPath = False):
    """
    获取当前路径下所有文件，文件名，递归查找
    :param rootDir:
    :return:
    """
    if os.path.isfile(rootDir):
        if addPath:
            return [rootDir]
        return [os.path.basename(rootDir)]
    fileLs = []
    for dir in os.listdir(rootDir):
        currentPath = os.path.join(rootDir, dir)
        fileLs.extend(listAllFiles(currentPath, addPath))
    return fileLs


def listFiles(rootDir, suffix=""):
    """
    获取当前路径下所有文件，文件名，仅一层目录，不递归查找
    :param rootDir: 根目录
    :param suffix: 扩展名
    :return: 文件列表
    """
    files = []
    for file in os.listdir(rootDir):
        if os.path.isfile(os.path.join(rootDir, file)):
            if os.path.splitext(file)[1] == suffix or suffix=="":
                files.append(file)
    return files

def getExtName(fileName):
    """
    获取文件扩展名
    :param fileName: 文件名
    :return: 扩展名
    """
    return os.path.splitext(fileName)[-1][1:]

def getExtName2(fileName:str):
    """
    获取后缀，第一个.后的字符串
    :param fileName: 文件名
    :return: 后缀
    """
    index = fileName.index(".")
    if index < 0:
        return ""
    return fileName[index+1:]

def getBaseName(fileName:str):
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

# def getfileName(filePath):
#     return os.path.basename(filePath)


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


def copyFile(srcFile, dstPath, infoFlag=False):
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
        print("Error: A file of the same name exists under the destination path.")
    shutil.copyfile(srcFile, dstfile)
    if infoFlag:
        print(os.path.realpath(srcFile) + "has been copied to " + os.path.realpath(dstPath))


def moveFile(srcFile, dstPath, infoFlag=False):
    if not os.path.isfile(srcFile):
        print("Error: " + os.path.realpath(srcFile) + " not exist.")
        return
    if os.path.normcase(os.path.dirname(srcFile)) == os.path.normcase(dstPath):
        print("Error: Copying files in the same directory is not supported.")
        return
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    dstFile = os.path.join(dstPath, os.path.basename(srcFile))
    if os.path.isfile(dstFile):
        print("Error: A file " + os.path.realpath(dstFile) + "of the same name exists under the destination path.")
    shutil.move(srcFile, dstFile)
    if infoFlag:
        print(os.path.realpath(srcFile) + "has been moved to " + os.path.realpath(dstPath))

if __name__ == '__main__':
    pass
