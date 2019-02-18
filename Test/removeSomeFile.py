#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/2/18 
# @Time    : 15:44
# @Author  : LinSicong
# @File    : removeSomeFile.py

import os
import glob
import cv2


if __name__ == '__main__':
    cot = 0
    path = "D:\Data\pigPose\CutPig"
    for ddir in os.listdir(path):
        temp_path = os.path.join(path, ddir)
        if os.path.isdir(temp_path):
            for pig_class in os.listdir(temp_path):
                ttemp_path = os.path.join(temp_path, pig_class)
                if os.path.isdir(ttemp_path):
                    images_list = glob.glob(os.path.join(ttemp_path, '*.jpg'))
                    for image_path in images_list:
                        bgr_image = cv2.imread(image_path)
                        if not hasattr(bgr_image, 'shape'):
                            print(image_path)
                            os.remove(image_path)
                            cot += 1
                            continue
    print("remove " + int(cot) + " images")
