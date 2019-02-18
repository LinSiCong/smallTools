#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/17 
# @Time    : 14:54
# @Author  : LinSicong
# @File    : ExcelToVideo.py

from dealExcel import dealExcel
from dealVideo import dealVideo
import cv2
import os

FPS = 25
JUMP_SECOND = 1 * FPS

CLASSES = ('A', 'B', 'C', 'D')


def dealFrame(frame, framenum, param):
    """
    对视频的单独帧进行处理
    :param frame: 一帧视频图像
    :param framenum: 帧数
    :param param: 参数表
    :return:
    """
    data = param[0]
    writeFlag = param[1]
    writePath = param[2]

    index = int(framenum / JUMP_SECOND)
    if index < 0:
        return frame
    row = data[index]
    if framenum == int(row[0]) - 1:
        box_score = row[2 : ]

        # 先截图，避免截取猪只时出现边框
        if writeFlag:
            for i in range(0, 4):
                coord = [int(float(x)) for x in box_score[i*5 : i*5+4]]
                score = float(box_score[i*5+4])
                # print(score)
                if score < 0:
                    continue
                p1 = (coord[0], coord[1])
                p2 = (coord[2], coord[3])

                cutImg = frame[coord[1]:coord[3], coord[0]:coord[2]] # [y1:y2, x1:x2]
                # cv2.imshow("test",cutImg)
                saveDir = os.path.join(writePath, CLASSES[i])
                if not os.path.isdir(saveDir):
                    os.makedirs(saveDir)
                savePath = os.path.join(saveDir, os.path.basename(writePath) + "_" + CLASSES[i] + "_" + str(framenum) + ".jpg")
                cv2.imwrite(savePath, cutImg)
                print("Save Image " + savePath)


        for i in range(0, 4):
            coord = [int(float(x)) for x in box_score[i*5 : i*5+4]]
            score = float(box_score[i*5+4])
            if score < 0:
                continue
            p1 = (coord[0], coord[1])
            p2 = (coord[2], coord[3])
            cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)
            p3 = (coord[0]+5, coord[3]-5)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, CLASSES[i] + " " + str(score), p3,  font, 1, (0, 0, 255), 3)
    return frame


def ExcelToVideo(excelFile, videoFile, rootPath):
    success, data = dealExcel.readData(excelPath, 1)
    if success:
        print(data)
    success, video = dealVideo.readVideo(videoPath)
    if not success:
        print("Read " + videoPath + " failed.")
        return

    videoName = os.path.basename(videoPath)

    param = []
    param.append(data[1:])
    writeFlag = True
    param.append(writeFlag)
    writePath = os.path.join(rootPath, "CutPig",os.path.splitext(videoName)[0])
    print(writePath)
    param.append(writePath)
    # dealVideo.showVideoWithFunc(video, True, param, func=dealFrame, step=JUMP_SECOND,  videoName=videoName, rate=0.5)
    detectionVideoPath = os.path.join(rootPath, "detectionVideo")
    if not os.path.isdir(detectionVideoPath):
        os.makedirs(detectionVideoPath)
    dealVideo.makeVideoFromVideo(video, detectionVideoPath, True, param, func=dealFrame, step=JUMP_SECOND, fps=2, videoName=os.path.splitext(videoName)[0] + "_d.avi")
    video.release()
    return


if __name__ == '__main__':
    rootPath = "D:/Data/pigClimb/"
    excelDir = os.path.join(rootPath, "FasterRcnn_result")
    videoDir = os.path.join(rootPath, "SourceVideo")
    fList = os.listdir(videoDir)
    for fileName in fList:
        if fileName == "01.avi":
            continue
        print("Read " + fileName + " and process")
        excelPath = os.path.join(excelDir, fileName + ".xls")
        videoPath = os.path.join(videoDir, fileName)
        ExcelToVideo(excelPath, videoPath, rootPath)
        print(fileName + " Done!")
