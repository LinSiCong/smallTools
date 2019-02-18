#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/17 
# @Time    : 17:27
# @Author  : LinSicong
# @File    : dealImage.py

import cv2



def resize(frame, rate):
    height = int(frame.shape[0] * rate)
    width = int(frame.shape[1] * rate)
    return cv2.resize(frame, (width, height))
