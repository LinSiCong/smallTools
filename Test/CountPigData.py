#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/2/22 
# @Time    : 19:51
# @Author  : LinSicong
# @File    : CountPigData.py

from dealExcel import ExcelProcessor
import os
import time

if __name__ == '__main__':
    xlsSaveDir = "D:\Data\pigPose\PoseData"
    countDtatSeveDir = "D:\Data\pigPose\PoseData2"
    xlsLs = os.listdir(xlsSaveDir)
    xlsLs.sort(key=lambda x:len(x))

    CLASSES = ('A', 'B', 'C', 'D')

    # 数据分成了两天
    # 前11个视频的时间从2016/07/15 06:23:10开始至2016/07/15 19:19:38
    # 第12个视频的时间从2016/07/20 18:09:04开始至2016/07/20 19:19:44
    # 后10个视频的时间从2016/07/16 07:04:26开始至2016/07/16 18:50:41
    cut = (11, 1, 10)
    timeTuple = [(2016, 7, 15, 6, 23, 10, 0, 0, 0), (2016, 7, 20, 18, 9, 4, 0, 0, 0), (2016, 7, 16, 7, 4, 26, 0, 0, 0)]
    conf = 0.7

    # 统计数据初始化
    pigData = []
    for i in range(4):
        tim = time.mktime(timeTuple[2])
        action = "None"
        pigData.append([CLASSES[i], tim, action, []])

    # 开始统计
    temp = 0
    for xls in xlsLs[12:]:
        OK, data = ExcelProcessor.readData(os.path.join(xlsSaveDir, xls))
        data = data[1:]
        print("-----------" + xls)
        for row in data:
            # 将字符串转化为时间戳
            tim = time.mktime(time.strptime(row[1],'%Y-%m-%d %H:%M:%S'))
            temp = tim

            for i in range(4):
                pig = row[i * 7 + 3 : i * 7 + 10]
                action = pig[5]
                if action == "None":
                    continue
                if float(pig[4]) < conf:
                    continue
                if xls == "021_pose.xls":
                    print(pig[6])
                if float(pig[6]) < conf:

                    continue
                # 数据初始化
                if pigData[i][2] == "None":
                    pigData[i][1] = tim
                    pigData[i][2] = action
                    continue
                if pigData[i][2] == action:
                    continue
                pigData[i][3].append([pigData[i][1], tim, pigData[i][2]])
                pigData[i][1] = tim
                pigData[i][2] = action


    for i in range(4):
        if pigData[i][1] == tim:
            continue
        pigData[i][3].append([pigData[i][1], tim, pigData[i][2]])
        pigData[i][1] = tim
        pigData[i][2] = action

    for i in range(4):
        data = [["时间(起始时间-结束时间)","持续时长(单位：秒）","行为"]]
        saveName = "20160716_" + CLASSES[i] + ".xls"
        for row in pigData[i][3]:
            st = row[0]
            ed = row[1]
            action = row[2]
            str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st)) + " - " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ed))
            ct = ed - st
            data.append([str, ct , action])
        ExcelProcessor.writeExcel(countDtatSeveDir, saveName, data)

    print("")