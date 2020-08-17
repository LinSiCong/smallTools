#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/10/31 
# @Time    : 21:29
# @Author  : LinSicong
# @File    : ForUTF8ErroCodes.py

import os

def utf8ToChinese(str):
    return str.encode('utf-8').decode('unicode_escape')

def resaveUTF8File(file_path):
    if not os.path.exists(file_path):
        print(file_path + " is not exist")
        return
    if not os.path.isfile(file_path):
        print(file_path + " is not a file")
        return
    with open(file_path, encoding="utf-8") as file:
        content = file.read()
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(utf8ToChinese(content))


    return


if __name__ == '__main__':

    resaveUTF8File("D:\Workspace\\transfer\\transfer_client\sysinfo.properties")