#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/3/1 
# @Time    : 16:28
# @Author  : LinSicong
# @File    : StringProcessor.py

import re


def readNums(str):
    """
    提取字符串中的数字，返回数字字符串列表
    :param str: 包含数字的字符串
    :return: 数字字符串列表
    """
    return re.findall(r"\d+\.?\d*", str)

def int2String(num, length):
    num = str(num)
    for i in range(len(num), length):
        num = '0' + num
    return num


if __name__ == '__main__':
    for i in range(0, 100):
        print(int2String(i, 3))