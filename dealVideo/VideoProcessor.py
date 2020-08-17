#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/16 
# @Time    : 21:04
# @Author  : LinSicong
# @File    : VideoProcessor.py

import cv2
import os
from dealImage import ImageProcessor


def readVideo(file):
    """
    Read a video by opencv.
    :param file: video path
    :return: videoCapture
    """
    if not os.path.exists(file):
        print(file + " is not exists.")
        return False, None
    return True, cv2.VideoCapture(file)


def showVideo(video, infoFlag, step=1, rate=1.0, videoName="video", winName='demo'):
    """
    播放视频，允许跳帧播放.允许调整播放比例
    Play the video. Jump by step. Press "Esc" to exit.
    :param video: cv2.VideoCapture
    :param infoFlag: if show info
    :param step: jump frame
    :param rate: resize rate
    :param videoName: video name
    :param winName: window name
    :return:
    """
    flag, frame = video.read()
    if not flag:
        print("Read video failed.")
        return

    frameNum = 0
    while flag:
        key = cv2.waitKey(1) & 0xff  # when you press "Esc" the video stop
        if key == 27:
            break
        if frameNum % step == 0:
            if infoFlag:
                print("Frame " + str(frameNum + 1) + " is showing.")
            cv2.imshow(winName, frame)
        frameNum += 1
        flag, frame = video.read()
    if infoFlag:
        if flag:
            print("Exit")
        else:
            print("The " + videoName + " has " + str(frameNum) + " frames.")
    print("End of " + videoName)


def demoFunc(frame, framenum=0, param=[]):
    return frame

def showVideoWithFunc(video, infoFlag, param, func=demoFunc, step=1, rate=1.0, videoName="video", winName='demo'):
    """
    播放视频，允许跳帧播放，允许自定义单帧图像处理函数，需提供参数列表，该函数要包含包括但帧图像，当前帧数，参数列表三个参数。
    Play the video. Jump by step. Press "Esc" to exit.Use func to process each frame.
    :param video: cv2.VideoCapture
    :param infoFlag: if show info
    :param func: A function to process each frame.It must contain 3 params: frame, frameNum, paramList and return frame.
    :param param: A param list for the function
    :param step: jump frame
    :param rate: resize rate
    :param videoName: video name
    :param winName: window name
    :return:
    """

    flag, frame = video.read()
    if not flag:
        print("Read video failed.")
        return

    frameNum = 0
    while flag:
        key = cv2.waitKey(1) & 0xff  # when you press "Esc" the video stop
        if key == 27:
            break
        if frameNum % step == 0:
            if infoFlag:
                print("Frame " + str(frameNum + 1) + " is showing.")
            frame = func(frame, frameNum, param)
            frame = ImageProcessor.resize(frame, rate)
            cv2.imshow(winName, frame)
        frameNum += 1
        flag, frame = video.read()
    if infoFlag:
        if flag:
            print("Exit")
        else:
            print("The " + videoName + " has " + str(frameNum) + " frames.")
    print("End of " + videoName)


def videoScissors(cap, picNum, start=0, step=1):
    """
    :param cap: 视频
    :param picNum: 剪辑帧数
    :param start: 起始帧
    :param step: 步进
    :return: 图片列表，每个项为一个二元组（图片，对应帧）
    """
    frameList = []
    success = cap.isOpened()  # 判断是否正常打开
    frameCount = 0
    picCount = 0
    while success:
        success, frame = cap.read()
        if frameCount >= start:
            if frameCount % step == 0:
                frameList.append((frame, frameCount))
                picCount = picCount + 1
        if picCount >= picNum:
            break
        frameCount = frameCount + 1
    return frameList


def makeVideoFromVideo(video, savePath, infoFlag, param, func=demoFunc, step=1, fps=1, videoName="video.avi"):
    """
    从视频中读取图片，做成视频
    :param video:
    :param savePath:
    :param infoFlag:
    :param param:
    :param func:
    :param step:
    :param fps:
    :param videoName:
    :return:
    """
    flag, frame = video.read()

    size = (frame.shape[1], frame.shape[0])
    videowriter = cv2.VideoWriter(os.path.join(savePath, videoName), cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps,
                                  size)

    if not flag:
        print("Read video failed.")
        return

    frameNum = 0
    while flag:
        if frameNum % step == 0:
            if infoFlag:
                print("Frame " + str(frameNum + 1) + " is processing.")
            frame = func(frame, frameNum, param)
            videowriter.write(frame)
        frameNum += 1
        flag, frame = video.read()
    print("Finish")
    return


def videoToImage(video, imgPath, step=1, func=demoFunc):
    """
    读取视频保存为图片集
    :param video: 视频
    :param imgPath: 图片集路径
    :param step:  跳帧步长
    :param func:  图片处理方式
    :return:
    """
    flag, frame = video.read()
    if not flag:
        print("Read video failed.")
        return
    if not os.path.exists(imgPath):
        os.makedirs(imgPath)
    frameNum = 0
    while flag:
        if frameNum % step == 0:
            frame = func(frame)
            cv2.imwrite(os.path.join(imgPath, str(frameNum) + '.jpg'), frame)
        frameNum += 1
        flag, frame = video.read()
    print("Finish")
    return


def videoToImageSelction(video, imgPath, selection, prefix, func=demoFunc):
    """
        读取视频，选取特定帧，保存为图片集
        :param video: 视频
        :param imgPath: 图片集路径
        :param selection 选择特定帧打印
        :param func:  图片处理方式
        :return:
        """
    flag, frame = video.read()
    if not flag:
        print("Read video failed.")
        return
    if not os.path.exists(imgPath):
        os.makedirs(imgPath)
    frameNum = 0
    index = 0
    while flag:
        if frameNum == selection[index]:
            frame = func(frame)
            cv2.imwrite(os.path.join(imgPath, prefix + str(frameNum) + '.jpg'), frame)
            index += 1
            if index >= len(selection):
                break
        frameNum += 1
        if index == len(selection):
            break
        flag, frame = video.read()
    print("Finish")
    return

def getVideoShape(video):
    return (video.get(3), video.get(5)) # (width, height)

def getVideoFrameNum(video):
    return int(video.get(7))  # 帧数

def getVideoFPS(video):
    return int(video.get(5)) # 帧速率

def getVideoTime(video):
    return getVideoFrameNum(video) / getVideoFPS(video) # 时长 second


if __name__ == '__main__':
    videoSrc = "D:\Data\pigPose\SourceVideo"
    videoPath = os.path.join("D:\Data\pigPose\sourceTestImg", "01.avi")
    ok, v = readVideo(os.path.join(videoSrc, "01.avi"))
    if ok:
        videoToImageSelction(v, videoPath, selection=[11100 + x * 25 for x in range(0, 3)])
