#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/8/2 
# @Time    : 15:36
# @Author  : LinSicong
# @File    : getFileList.py

import os
import glob

def listDirPath(rootDir, suffix=''):
    return glob(rootDir + "/*" + suffix)

def listDir(rootDir, suffix='jpg'):
    files = []
    for lists in os.listdir(rootDir):
        if lists[-len(suffix):] == suffix:
            files.append(lists)
    return files

def getFileList(rootDir):
    fileList = os.listdir(rootDir)
    newFileList = []
    for name in fileList:
        if os.path.isfile(os.path.join(rootDir, name)):
            if name != "getFileList.py":
                newFileList.append(os.path.splitext(name)[0])
    print("Read " + str(len(newFileList)) + " files.")
    return newFileList


def generateFileListFile(rootDir, outputFileName):
    fileList = getFileList(rootDir)
    outFile = open(outputFileName, "w")
    for name in fileList:
        outFile.write(name + "\n")
    outFile.close()


if __name__ == '__main__':
    workDir = "D:\\Data\\beedata\\new\\annotation" #os.getcwd()           #获取当前工作目录
    outFile = "fileList.txt"
    generateFileListFile(workDir, outFile)
