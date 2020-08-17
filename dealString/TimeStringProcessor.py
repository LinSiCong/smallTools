#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/3/5 
# @Time    : 16:26
# @Author  : LinSicong
# @File    : TimeStringProcessor.py


import time

def time_demo():
    """
    关于time模块的使用说明
    :return:
    """
    struct_time = time.strptime("30 Nov 00", "%d %b %y")
    print("返回的元组: %s " % struct_time)
    # 返回的元组: time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
    # 时间元组结构说明： tm_year 年 tm_mon 月 tm_hour 时  tm_min 分, tm_sec 秒, tm_wday 一周第几天（0-6，0表示周一）, tm_yday 一年第几天（1-366）, tm_isdst 是否夏令时（Daylight Saving Time）

def stringToTime(timStr, pattern='%Y-%m-%d %H:%M:%S'):
    """
    将字符串格式化为时间戳
    :param timStr: 字符串
    :param pattern: 时间格式
    :return: 时间戳(秒数表示时间的浮点数)
    """
    return time.mktime(time.strptime(timStr, pattern))


def timeToString(tim, pattern='%Y-%m-%d %H:%M:%S'):
    """
    将时间戳格式化为字符串
    :param tim: 时间戳
    :param pattern: 时间格式
    :return: 时间字符串
    """
    return time.strftime(pattern, time.localtime(tim))