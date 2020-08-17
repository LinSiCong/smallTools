#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/5/10 
# @Time    : 16:27
# @Author  : LinSicong
# @File    : ReadConfig.py

import configparser

class ReadConfig:
    def __init__(self, file_path):
        self.cf = configparser.ConfigParser()
        self.cf.read(file_path, encoding='utf-8')

    def __getCF__(self):
        return self.cf

    def get_sections(self):
        return self.cf.sections()

    def get_options(self, section):
        return self.cf.options(section)

    def read_config(self, section, option):
        return self.cf.get(section, option)

    """read config file"""
    def read_config_file(self, file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8")
        res = cf.get(section, option)
        return res


class dealConfig:
    def __init__(self, cf = None):
        if cf == None:
            cf = configparser.ConfigParser()
        self.cf = cf

    def __getCF__(self):
        return self.cf

    def create_config_file(self, file_path):
        self.cf.write(open(file_path, 'w'))

    def write_config(self, section, option, value):
        if not self.cf.has_section(section):
            self.cf.add_section(section)
        self.cf.set(section, option, value)

class MyPathConfig:
    def __init__(self, root_path):
        pass

    def __new__(cls, *args, **kwargs):
        """
        单例
        """
        if not hasattr(MyPathConfig, "_instance"):
            with MyPathConfig._instance_lock:
                if not hasattr(MyPathConfig, "_instance"):
                    MyPathConfig._instance = object.__new__(cls)
        return MyPathConfig._instance

if __name__ == '__main__':
    config_path = "../testspace/project.conf"
    cf = dealConfig()
    cf.write_config("Path","root", "D:\PycharmProjects")
    cf.write_config("Path","config", "\\testspace\\project.conf")
    cf.write_config("Path", "img", "\\testspace\\img")
    cf.write_config("Path", "video", "\\testspace\\video")
    cf.create_config_file(config_path)

    readCf = ReadConfig(config_path)
    for section in readCf.get_sections():
        for option in readCf.get_options(section):
            print(readCf.read_config(section, option))



