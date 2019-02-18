#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/16 
# @Time    : 20:51
# @Author  : LinSicong
# @File    : useVideoScissors.py

from dealVideo.dealVideo import videoScissors
import cv2
import os


rootPath = "D:\\Data\\pigdata\\"
datasetID = 6
videoPath = rootPath + str(datasetID) + "\\Video"
picSavePath = rootPath + str(datasetID) + "\\JPEGImages"
totalNum = 100

count = 0
videoList = os.listdir(videoPath)
numPerVideo = totalNum / len(videoList)

for videoName in videoList:
    video = cv2.VideoCapture(videoPath + "\\" + videoName)
    print("Roading....." + videoPath + "\\" + videoName)
    picList = videoScissors(video, numPerVideo, step=50)
    video.release()
    print("Writing File")
    for i in range(0, len(picList)):
        count = count + 1
        frame = picList[i][0]
        cv2.imwrite(picSavePath + '\\' + str(count) + '.jpg', frame)
    print("Write " + str(len(picList)) + " pictures")
print("Finish")
