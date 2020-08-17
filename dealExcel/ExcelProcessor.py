#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/16 
# @Time    : 15:27
# @Author  : LinSicong
# @File    : ExcelProcessor.py

import xlrd
import xlwt
import os
import functools


def readWorkbook(file):
    """
    Read a workbook from Excel file that contains multiple tables.
    :param file: File Path
    :return: Success Flag, workbook
    """
    if not os.path.exists(file):
        print(file + " is not exists.")
        return False, None
    if not (file[-3:] == 'xls' or file[-4:] == '.xlsx'):
        print(file + " is not a excel file.")
        return False, None
    workbook = xlrd.open_workbook(file)
    # print(workbook.sheet_names())
    return True, workbook


def readSheet(file, sheetId = 1):
    """
        Read a sheet from Excel file
        :param file: File Path
        :param sheetId: The number of sheet
        :return: Success Flag, sheet
    """
    flag, workbook = readWorkbook(file)
    if not flag:
        return False, None
    sheetList = workbook.sheets()
    if len(sheetList) < sheetId or sheetId <= 0:
        print("There is no Sheet " + str(sheetId))
        return False, None
    return True, sheetList[sheetId - 1]

def readData(file, sheetId = 1):
    """
    Read data from a Excel sheet (as a list)
    :param file: File Path
    :param sheetId: The number of sheet
    :return: Success Flag, data
    """
    flag, sheet = readSheet(file, sheetId)
    if not flag:
        return False, None
    data = []
    for i in range(0, sheet.nrows):
        data.append(sheet.row_values(i))
    print(file + " is read.")
    return True, data


def writeExcel(xlsPath, xlsName, data, sheetName="Sheet1"):
    """
    Write data in Excel sheet
    :param xlsPath: dir path
    :param xlsName: xls file name
    :param data: data (a list)
    :param sheetName: sheet name
    :return: void
    """
    if not os.path.exists(xlsPath):
        os.makedirs(xlsPath)
        print("Create path " + xlsPath)
    xlsFile = os.path.join(xlsPath, xlsName)
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet(sheetName)
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            sheet.write(i, j, str(data[i][j]))
    workbook.save(xlsFile)
    print(xlsFile + " finish write.")

def demoFunc(data):
    def sortDemo(a, b):
        """
        升序排序算子
        """
        if a < b:
            return -1
        if a > b:
            return 1
        return 0
    return sorted(data, key=functools.cmp_to_key(sortDemo))


def dealData(readPath, writePath, sheetID=1, func=demoFunc):
    ok, data = readData(readPath, sheetID)
    if not ok:
        return
    data = func(data)
    xlsName = os.path.basename(writePath)
    xlsPath = os.path.dirname(writePath)
    writeExcel(xlsPath, xlsName, data)
    return

if __name__ == '__main__':
    def deldata(data):
        for i in range(len(data) - 1, 0, -1):
            if int(data[i][2]) % (25 * 5) == 0:
                continue
            print(data[i])
            del data[i]
        return data

    srcPath = "D:\Data\pigPose\\PoseData"
    dstPath = "D:\Data\pigPose\\temp"
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    ls = ['A', 'B', 'C', 'D']
    num = ['021', '022']
    for n in num:
        name = n + "_pose.xls"
        dealData(os.path.join(srcPath, name), os.path.join(dstPath, name), func=deldata)


