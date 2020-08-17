#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/10/15 
# @Time    : 9:39
# @Author  : LinSicong
# @File    : demo2.py

import asyncio
import os

rootPath = "D:\PycharmProjects\smallTools\\testspace"

async def change_files(x):
    files = os.listdir(rootPath)
    for filename in files:
        portion = os.path.splitext(filename)
        if portion[1] == ".test":
            print(portion)
            newname = portion[0] + '.txt'
            os.chdir(rootPath)
            os.rename(filename, newname)
    return '{}任务完成'.format(x)

def callback(future):
    print("Callback: ", future.result())

coroutine = change_files("修改扩展名")
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
loop.run_until_complete(task)


