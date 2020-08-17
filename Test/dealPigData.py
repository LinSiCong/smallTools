#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/2/21 
# @Time    : 19:43
# @Author  : LinSicong
# @File    : dealPigData.py

from dealExcel import ExcelProcessor
import os
import time

test = False

if __name__ == '__main__':
    sourceDir = "D:\Data\pigPose\FasterRcnn_result"
    xlsDir = "D:\Data\pigPose\\posResult"
    xlsSaveDir = "D:\Data\pigPose\PoseData"

    timeTupleList = \
    [(2016, 7, 15, 6, 23, 5, 0, 0, 0),
     (2016, 7, 15, 7, 33, 24, 0, 0, 0),
     (2016, 7, 15, 8, 43, 46, 0, 0, 0),
     (2016, 7, 15, 9, 54, 29, 0, 0, 0),
     (2016, 7, 15, 11, 5, 23, 0, 0, 0),
     (2016, 7, 15, 12, 16, 33, 0, 0, 0),
     (2016, 7, 15, 13, 27, 33, 0, 0, 0),
     (2016, 7, 15, 14, 38, 1, 0, 0, 0),
     (2016, 7, 15, 15, 48, 24, 0, 0, 0),
     (2016, 7, 15, 16, 58, 46, 0, 0, 0),
     (2016, 7, 15, 18, 9, 8, 0, 0, 0),
     (2016, 7, 20, 18, 8, 59, 0, 0, 0),             # 第12个视频不知道为什么是20号的
     (2016, 7, 16, 7, 4, 21, 0, 0, 0),
     (2016, 7, 16, 8, 14, 42, 0, 0, 0),
     (2016, 7, 16, 9, 25, 24, 0, 0, 0),
     (2016, 7, 16, 10, 36, 3, 0, 0, 0),
     (2016, 7, 16, 11, 47, 16, 0, 0, 0),
     (2016, 7, 16, 12, 58, 29, 0, 0, 0),
     (2016, 7, 16, 14, 9, 13, 0, 0, 0),
     (2016, 7, 16, 15, 19, 36, 0, 0, 0),
     (2016, 7, 16, 16, 29, 57, 0, 0, 0),
     (2016, 7, 16, 17, 40, 16, 0, 0, 0)
     ]
    CLASSES = ('A', 'B', 'C', 'D')

    dirls = os.listdir(sourceDir)
    dirls.sort(key=lambda i: len(i))

    # 整合数据
    title = []
    title.append('Source Video')
    title.append('Time')
    title.append('frame')
    for i in range(4):
        title.append(CLASSES[i] + ".UL.x")
        title.append(CLASSES[i] + ".UL.y")
        title.append(CLASSES[i] + ".LR.x")
        title.append(CLASSES[i] + ".LR.y")
        title.append(CLASSES[i] + ".loc.score")
        title.append(CLASSES[i] + ".pose")
        title.append(CLASSES[i] + ".pose.score")

    # 循环读取视频中四头猪的数据表
    for dir in dirls:
        numStr = str.split(dir, '.')[0]
        num = int(numStr)
        if num != 21 and num != 22:
            continue

        st = time.mktime(timeTupleList[num - 1])
        # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(st)))

        if not test or num == 1:
            OK, srcData = ExcelProcessor.readData(os.path.join(sourceDir, dir))

            # 读取相应视频四头猪的姿态检测数据
            pigDataLs = []
            for i in range(4):
                xlsPath = os.path.join(xlsDir, numStr + "_" + CLASSES[i] +".xls")
                OK, pigData = ExcelProcessor.readData(xlsPath)
                for i in range(len(pigData)):
                    # pigData[i][0] = int(os.path.basename(pigData[i][0])[:-4])
                    pigData[i][0] = int(os.path.basename(pigData[i][0]).split('_')[-1].split('.')[0])

                # pigData.sort(key=lambda x:x[0])
                # print(pigData[0])
                pigDataLs.append(pigData)

            # 开始整合
            xlsData = [title]
            for row in srcData[1:]:
                frame = int(row[0])
                sec = row[1]
                tim = st + float(sec)

                xlsDataRow = []
                xlsDataRow.append(numStr + ".avi")
                xlsDataRow.append(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tim)))
                xlsDataRow.append(frame)
                # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tim)))
                for i in range(4):
                    temp = row[i * 5 + 2 : i * 5 + 7]
                    # print(CLASSES[i] + " : " + str(temp))
                    xlsDataRow.extend(temp)
                    poseData = []
                    if temp[-1] == "-1":
                        poseData.append("None")
                        poseData.append(-1)
                    else:
                        """
                        这代码真TM暴力,下次用求你改改 --sc 2019.03.19 23:20
                        居然被这代码救了一命，暴力出奇迹 --sc 2019.03.20 2:14
                      """
                        flag = False
                        for it in range(len(pigDataLs[i])):
                            if pigDataLs[i][it][0] == frame - 1:
                                poseData.append(pigDataLs[i][it][1])
                                poseData.append(float('%.2f' % float(pigDataLs[i][it][2])))
                                flag = True
                                break
                        if not flag:
                            poseData.append("Error")
                            poseData.append("Error")

                    xlsDataRow.extend(poseData)
                xlsData.append(xlsDataRow)

            ExcelProcessor.writeExcel(xlsSaveDir, numStr + "_pose.xls", xlsData)
            print("----------")