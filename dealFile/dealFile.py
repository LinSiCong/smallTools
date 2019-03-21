#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/22 
# @Time    : 18:12
# @Author  : LinSicong
# @File    : dealFile.py


import os


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


"[VCB-Studio] Bungo Stray Dogs [01][Ma10p_1080p][x265_flac]"

if __name__ == '__main__':
    path = "D:\Downloads\文豪野犬24集全\新建文件夹"
    renameAllFile(path, prefix="[VCB-Studio] Bungo Stray Dogs [0", suffix="][Ma10p_1080p][x265_flac]", mode=1,
                  type=".ass", startID=12, sort=True)