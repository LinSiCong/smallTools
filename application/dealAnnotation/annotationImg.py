#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/4/3 
# @Time    : 18:03
# @Author  : LinSicong
# @File    : annotationImg.py

import os
import cv2

"""
    在图像中标记annotation
"""

def annotationOnImg(img, label, box, score=None, thickness=2, color=(0, 0, 255), isText=True, fontColor=(0, 0, 255),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, fontThickness=1):
    tempImg = img.copy()
    p1 = (box[0], box[1])
    p2 = (box[2], box[3])
    cv2.rectangle(tempImg, p1, p2, color, thickness)
    if isText:
        p3 = (box[0] + 5, box[3] - 5)
        if score != None:
            cv2.putText(tempImg, label + " " + str(score), p3, fontFace, fontScale, fontColor, fontThickness)
        else:
            cv2.putText(tempImg, label + " ", p3, fontFace, fontScale, fontColor, fontThickness)
    return tempImg

if __name__ == '__main__':
    srcPath = "D:\PycharmProjects\smallTools\\testspace\img\pig3"
    ImgName = "076.avi_71058.jpg"
    color = [
        (0, 0 ,255),
        (0, 255, 255),
        (255, 255, 0),
        (255, 0, 0),
        (0, 255, 0)
    ]

    pigLs = [
        # [970, 1013, 1658, 1314, 1.0],
        # [1111, 233, 1787, 504, 0.99],
        # [1587, 136, 2253, 580, 1.0],
        [1530, 631, 2158, 875, 0.98]
    ]

    headLs = [
        # [973, 1028, 1175, 1230, 1.0],
        # [],
        # [2065, 141, 2264, 350, 0.98],
        [1976, 636, 2155, 819, 0.99]
    ]

    backLs = [
        # [1209, 1195, 1356, 1294, 1.0],
        # [1333, 231, 1514, 336, 0.99],
        # [1810, 256, 1944, 371, 1.0],
        [1791, 673, 1946, 794, 0.98]

    ]

    tailLs = [
        # [1487, 1114, 1650, 1302, 0.97],
        # [1129, 249, 1307, 450, 0.99],
        # [1593, 392, 1809, 558, 1.0],
       # [1466, 672, 1654, 867, 1.0]
    ]

    fontColor = (0, 255, 255)

    img = cv2.imread(os.path.join(srcPath,ImgName))
    #
    # for data in pigLs:
    #     index = pigLs.index(data)
    #     cv2.imwrite(os.path.join(srcPath, "0123.avi_81565_pig" + str(index) + ".jpg"),
    #                 img[data[1]:data[3], data[0]: data[2]])
    #
    # for data in headLs:
    #     cv2.imwrite(os.path.join(srcPath, "0123.avi_81565_head" + str(headLs.index(data)) + ".jpg"),
    #                 img[data[1]:data[3], data[0]: data[2]])
    #
    # for data in backLs:
    #     cv2.imwrite(os.path.join(srcPath, "0123.avi_81565_back" + str(backLs.index(data)) + ".jpg"),
    #                 img[data[1]:data[3], data[0]: data[2]])
    #
    # for data in tailLs:
    #     cv2.imwrite(os.path.join(srcPath, "0123.avi_81565_tail" + str(tailLs.index(data)) + ".jpg"),
    #                 img[data[1]:data[3], data[0]: data[2]])
    #
    # for data in pigLs:
    #     timg = img
    #     index = pigLs.index(data)
    #     timg = annotationOnImg(timg, "head", headLs[index][:4], fontThickness=2, fontColor=(0, 255, 255),
    #                            color=color[index])
    #     timg = annotationOnImg(timg, "back", backLs[index][:4], fontThickness=2, fontColor=(0, 255, 255),
    #                            color=color[index])
    #     timg = annotationOnImg(timg, "tail", tailLs[index][:4], fontThickness=2, fontColor=(0, 255, 255),
    #                            color=color[index])
    #     cv2.imwrite(os.path.join(srcPath, "0123.avi_81565_pig_and_more" + str(index) + ".jpg"),
    #                 timg[data[1]:data[3], data[0]: data[2]])
    #
    for data in pigLs:
        if len(data) < 5:
            continue
        img = annotationOnImg(img, "pig", data[:4], fontThickness=2, fontColor=fontColor, color=color[pigLs.index(data)])
    #
    # cv2.imwrite(os.path.join(srcPath, "0123.avi_81565_pigs.jpg"), img)
    # cv2.imwrite(os.path.join(srcPath, "0123.avi_81565_pigs_cut.jpg"), img[:, 1200:])
    #
    #
    for data in headLs:
        if len(data) < 5:
            continue
        img = annotationOnImg(img, "head", data[:4], fontThickness=2, fontColor=fontColor, color=color[headLs.index(data)])

    for data in tailLs:
        if len(data) < 5:
            continue
        img = annotationOnImg(img, "tail", data[:4], fontThickness=2, fontColor=fontColor, color=color[tailLs.index(data)])

    for data in backLs:
        if len(data) < 5:
            continue
        img = annotationOnImg(img, "back", data[:4], fontThickness=2, fontColor=fontColor, color=color[backLs.index(data)])

    cv2.imwrite(os.path.join(srcPath, "076.avi_71058_D.jpg"), img)

"""
# 0123.avi_81565.jpg
# bad data
    pigLs = [
        [1536, 197, 2110, 426, 1.0],
        [1716, 356, 2138, 813, 0.99],
        [1575, 855, 2121, 1091, 1.0],
        [1579, 1066, 2109, 1348, 0.98]
    ]

    headLs = [
        [1933, 204, 2085, 375, 1.0],
        [1953, 352, 2120, 521, 0.98],
        [1991, 887, 2119, 1074, 0.99],
        [1954, 1071, 2135, 1289, 1.0]
    ]

    backLs = [
        [1767, 198, 1928, 314, 1.0],
        [1940, 502, 2055, 629, 0.99],
        [1867, 927, 2022, 1061, 1.0],
        [1857, 1201, 2009, 1302, 0.98]
    ]

    tailLs = [
        [1517, 187, 1686, 362, 1.0],
        [1707, 633, 1890, 808, 1.0],
        [1563, 879, 1733, 1075, 0.99],
        [1581, 1152, 1736, 1341, 0.98]
    ]
    
# good data
    pigLs = [
        [1513, 187, 2110, 426, 1.0],
        [1716, 350, 2138, 813, 0.99],
        [1560, 855, 2121, 1091, 1.0],
        [1579, 1066, 2135, 1348, 0.98]
    ]

    headLs = [
        [1933, 204, 2085, 375, 1.0],
        [1953, 352, 2120, 521, 0.98],
        [1991, 887, 2119, 1074, 0.99],
        [1954, 1071, 2135, 1289, 1.0]
    ]

    backLs = [
        [1767, 198, 1928, 314, 1.0],
        [1940, 502, 2055, 629, 0.99],
        [1867, 927, 2022, 1061, 1.0],
        [1857, 1201, 2009, 1302, 0.98]
    ]

    tailLs = [
        [1517, 187, 1686, 362, 1.0],
        [1720, 633, 1890, 808, 1.0],
        [1563, 879, 1733, 1075, 0.99],
        [1581, 1152, 1736, 1341, 0.98]
    ]
"""

"""
# 0115.avi_25572.jpg

# good data
    pigLs = [
        [935, 917, 1590, 1297, 1.0],
        [894, 479, 1397, 1060, 0.99],
        [1353, 223, 2007, 473, 1.0],
        [1662, 370, 1981, 986, 0.98]
    ]

    headLs = [
        [943, 942, 1140, 1129, 1.0],
        [1155, 867, 1352, 1058, 0.99],
        [1815, 246, 2000, 427, 0.98],
        []
    ]

    backLs = [
        [1193, 1137, 1366, 1253, 1.0],
        [1062, 587, 1213, 749, 0.99],
        [1592, 241, 1753, 331, 1.0],
        [1887, 591, 1970, 728, 0.98]

    ]

    tailLs = [
        [1407, 1118, 1585, 1294, 1.0],
        [910, 480, 1094, 621, 0.99],
        [1359, 264, 1503, 451, 1.0],
        [1731, 830, 1944, 982, 1.0]
    ]
    
# A头部误检
    pigLs = [
        [935, 917, 1590, 1297, 1.0],
        [894, 479, 1397, 1060, 0.99],
        [1353, 223, 2007, 473, 1.0],
        [1662, 370, 1981, 986, 0.98]
    ]

    headLs = [
        [1155, 923, 1352, 1058, 1.0],   # A头部误检
        [1155, 867, 1352, 1058, 0.99],
        [1815, 246, 2000, 427, 0.98],
        []
    ]

    backLs = [
        [1193, 1137, 1366, 1253, 1.0],
        [1062, 587, 1213, 749, 0.99],
        [1592, 241, 1753, 331, 1.0],
        [1887, 591, 1970, 728, 0.98]

    ]

    tailLs = [
        [1407, 1118, 1585, 1294, 1.0],
        [910, 480, 1094, 621, 0.99],
        [1359, 264, 1503, 451, 1.0],
        [1731, 830, 1944, 982, 1.0]
    ]

    
"""
"""
# 076.avi_71058.jpg
# good data
    pigLs = [
        [970, 1013, 1658, 1314, 1.0],
        [1111, 233, 1787, 504, 0.99],
        [1587, 136, 2253, 580, 1.0],
        [1460, 631, 2158, 875, 0.98]
    ]

    headLs = [
        [973, 1028, 1175, 1230, 1.0],
        [],
        [2065, 141, 2264, 350, 0.98],
        [1976, 636, 2155, 819, 0.99]
    ]

    backLs = [
        [1209, 1195, 1356, 1294, 1.0],
        [1333, 231, 1514, 336, 0.99],
        [1810, 256, 1944, 371, 1.0],
        [1791, 673, 1946, 794, 0.98]

    ]

    tailLs = [
        [1487, 1114, 1650, 1302, 0.97],
        [1129, 249, 1307, 450, 0.99],
        [1593, 392, 1809, 558, 1.0],
        [1466, 672, 1654, 867, 1.0]
    ]
    # 边框回归错误    
    pigLs = [
        # [970, 1013, 1658, 1314, 1.0],
        # [1111, 233, 1787, 504, 0.99],
        # [1587, 136, 2253, 580, 1.0],
        [1530, 631, 2158, 875, 0.98]
    ]

    headLs = [
        # [973, 1028, 1175, 1230, 1.0],
        # [],
        # [2065, 141, 2264, 350, 0.98],
        [1976, 636, 2155, 819, 0.99]
    ]

    backLs = [
        # [1209, 1195, 1356, 1294, 1.0],
        # [1333, 231, 1514, 336, 0.99],
        # [1810, 256, 1944, 371, 1.0],
        [1791, 673, 1946, 794, 0.98]

    ]

    tailLs = [
        # [1487, 1114, 1650, 1302, 0.97],
        # [1129, 249, 1307, 450, 0.99],
        # [1593, 392, 1809, 558, 1.0],
       # [1466, 672, 1654, 867, 1.0]
    ]
"""