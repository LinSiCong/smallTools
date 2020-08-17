#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/9 
# @Time    : 10:08
# @Author  : LinSicong
# @File    : dealCommand.py
"""
读取命令行输入的参数（主要是介绍argparse的用法）
"""

import sys
import argparse

def readArguments():
    parser = argparse.ArgumentParser(description='Test.')
    parser.add_argument('a', help='First parameter')                # 必要参数，不需要在指定
    # parser.add_argument('a', help='First parameter', nargs='?')       # nargs指定参数个数，如果nargs='?'说明这个参数可带可不带
    # 特别的，nargs=1生成一个只有一个元素的列表。这和默认的行为是不一样的，默认情况下生成的是元素自己

    parser.add_argument('--b', dest='b', help='Second parameter', default=99, type=type("99"))
                                                                    # dest指定parse_args()返回的对象要添加的属性名称
                                                                    # default指定默认值
                                                                    # type指定命令行参数应该被转换成的类型

    parser.add_argument('-c', '--cc', help='Third parameter')     # 参数的前面可以添加‘-’（简称），也可以添加‘--’（全称）
                                                                     # 说明添加的参数可以用简写也可以用全称来标明。但是解析的时候必须用全称

    parser.add_argument('--d', dest='d', help='Choice test.[1, 2, 3]', choices=['1','2','3'], required=True)
                                                                    # choices提供可选参数
                                                                    #required表示该命令行选项是否可以省略（只针对可选参数）


    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()

if __name__ == '__main__':
    args = readArguments()
    print(args.a)
    print(args.b)
    print(type(args.b))
    print(args.cc)
    print(args.d)