#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/7/5 
# @Time    : 10:27
# @Author  : LinSicong
# @File    : getDatasetFromVideoList.py

"""
    从一个视频文件夹，随机抽取视频，对一个视频选取随机帧，保存图片，作为数据集
"""
from dealFile import getFileList
import dealVideo
import random
import os

datasetSize = 3000
videoRoot = "F:\猪实验相关数据资料\\avi"
datasetRoot = "D:\Data\pigTrack\detect\JPEGImages"
existVideo = ["022.avi","028.avi","051.avi, 070.avi", "0115.avi", "0119.avi", "0122.avi", "0130.avi"]
nightVideo = ["0126.avi", "0128.avi"]

if __name__ == '__main__':

    videoList = getFileList.listDir(videoRoot, ".avi")
    videoList = random.sample(videoList, 4)

    for videoName in videoList:
        print(videoName)
        if videoName in existVideo:
            continue
        if videoName in nightVideo:
            continue
        flag, video = dealVideo.readVideo(os.path.join(videoRoot, videoName))
        if flag:
            frameNum = dealVideo.getVideoFrameNum(video)
            fps = dealVideo.getVideoFPS(video)
            space = 20
            generateNum = min(int(frameNum / (fps * space)), 100)
            frameList = list(fps * space * x + random.randint(0, space * fps) for x in random.sample(range(0, int(frameNum / (fps * space))), generateNum))
            frameList.sort()
            # print(frameList)
            print(len(frameList))
            dealVideo.videoToImageSelction(video, datasetRoot, frameList, videoName + "_")