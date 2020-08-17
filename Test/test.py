#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/22 
# @Time    : 18:29
# @Author  : LinSicong
# @File    : test.py

import os

name = ["最优化方法（省研究生示范课程）", "计算机科学与技术学科进展", "计算机视觉", "数据仓库与数据挖掘",
        "算法设计与分析	", "人工智能", "组合数学", "硕士生英语", "中国特色社会主义理论与实践研究", "自然辩证法概论"]
grade = [98, 94, 93, 81, 86, 93, 92, 95, 91, 88]
credit = [3, 2, 2, 2, 3, 3, 3, 3, 2, 1]


def tran_G(grade):
    return (grade - 50) * 1.0 / 10


def cal_GPA(grade, credit):
    zipped = zip(grade, credit)
    tot = 0.0
    for g, c in zipped:
        tot = tot + tran_G(g) * c
    s = sum(credit) * 1.0
    return tot / s


if __name__ == '__main__':
    gpa = cal_GPA(grade, credit)

    print()

    # for i, val in enumerate(zip(name, credit, grade)):
    #     print(str(i + 1) + ". 课程名称:",val[0],"学分:",val[1],"成绩:",val[2])
