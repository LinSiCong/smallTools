#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020/8/18 
# @Time    : 0:09
# @Author  : LinSicong
# @File    : cut_image_with_label.py
from xml.dom import minidom

import cv2
from dealImage import ImageProcessor
from dealFile import  FileProcessor
from  dealXML import dealXML
import os

root_path = "D:\PycharmProjects\smallTools\\testspace\pest"
src_img_dir = root_path
src_annotation_dir = root_path
save_img_dir_name = "cut_img"
save_ano_dir_name = "cut_annotation"

def read_img_list(dir_path):
    img_name_ls = []
    for img_name in os.listdir(dir_path):
        if FileProcessor.getExtName(img_name) == "jpg":
            img_name_ls.append(img_name)
    return  img_name_ls

# 计算切割区域
def count_cut_area(w_rate, h_rate, img_shape):
    img_w = img_shape[0]
    w_point = list([i * (img_w // w_rate) for i in range(0, w_rate)])
    w_point.append(img_w - 1)
    len_w = len(w_point)

    img_h = img_shape[1]
    h_point = list([i * (img_h // h_rate) for i in range(0, h_rate)])
    h_point.append(img_h - 1)
    len_h = len(h_point)

    grid_row = []
    for x in range(len_w):
        grid_col = []
        for y in range(len_h):
            grid_col.append((w_point[x], h_point[y]))
        grid_row.append(grid_col)
    area_list = []
    for i in range(len_w - 1):
        for j in range(len_h - 1):
            area_list.append((grid_row[i][j], grid_row[i+1][j+1]))
    return area_list

# 根据切割区域切割图片
def cut_img_scale(area, img):
    left_up = area[0]
    rigth_down = area[1]
    return ImageProcessor.cutImg(img, left_up, rigth_down)

# 获取所有object标签
def get_label_list(annotation_path):
    dom = dealXML.readXML(annotation_path)
    return dealXML.findXMLLabel(dom, "object")

# 获取size：
def get_anotation_shape(annotation_path):
    dom = dealXML.readXML(annotation_path)
    width = dealXML.getOnlyValue(dom, "width")
    height = dealXML.getOnlyValue(dom, "height")
    depth = dealXML.getOnlyValue(dom, "depth")
    return (width, height, depth)

# 判断标签和图片的size是否翻转
def check_flip(img_shape, ano_shape):
    if img_shape[0] == ano_shape[0] and img_shape[1] == ano_shape[1]:
        return False
    return True

# 获取object标签中的bndbox，返回左上，右下坐标二元组
def get_bndbox(label, is_flip):
    xmin = int(dealXML.getOnlyValue(label, "xmin"))
    ymin = int(dealXML.getOnlyValue(label, "ymin"))
    xmax = int(dealXML.getOnlyValue(label, "xmax"))
    ymax = int(dealXML.getOnlyValue(label, "ymax"))
    if is_flip:
        return ((ymin, xmin), (ymax, xmax))
    return ((xmin, ymin), (xmax, ymax))

# 判断bndbox是否在区域内
def check_area_inside(bndbox, area):
    return check_point_inside(bndbox[0], area) and check_point_inside(bndbox[1], area)

# 判断点是否在区域内
def check_point_inside(point, area):
    x = point[0]
    y = point[1]
    left_up = area[0]
    right_down = area[1]
    if x >= left_up[0] and x <= right_down[0] and y >= left_up[1] and y <= right_down[1]:
        return True
    return False

# 对bndbox进行偏移
def bndbox_offset(bndbox, offset):
    left_up = bndbox[0]
    right_down = bndbox[1]
    xmin = left_up[0] - offset[0]
    ymin = left_up[1] - offset[1]
    xmax = right_down[0] - offset[0]
    ymax = right_down[1] - offset[1]
    return ((xmin, ymin), (xmax, ymax))

# 修改objec标签中，bndbox的值
def modeify_object_label(label, bndbox, is_flip):
    left_up = bndbox[0]
    right_down = bndbox[1]
    if is_flip:
        dealXML.setXMLLabel(label, "xmin", str(left_up[1]))
        dealXML.setXMLLabel(label, "ymin", str(left_up[0]))
        dealXML.setXMLLabel(label, "xmax", str(right_down[1]))
        dealXML.setXMLLabel(label, "ymax", str(right_down[0]))
    else:
        dealXML.setXMLLabel(label, "xmin", str(left_up[0]))
        dealXML.setXMLLabel(label, "ymin", str(left_up[1]))
        dealXML.setXMLLabel(label, "xmax", str(right_down[0]))
        dealXML.setXMLLabel(label, "ymax", str(right_down[1]))

# 根据切割区域处理Annotation文件
def cut_annotation_scale(area, label_list, is_flip):
    cut_label_list = []
    for label in label_list:
        bndbox = get_bndbox(label, is_flip)
        if check_area_inside(bndbox, area):
            modeify_object_label(label, bndbox_offset(bndbox, area[0]), is_flip)
            cut_label_list.append(label)
    return cut_label_list


# 生成标签文件
def generate_annotation(object_list, img_name, img_path, is_filp, img_shape):
    dom = minidom.Document()

    annotation_label = dom.createElement("annotation")

    folder_label = dom.createElement("folder")
    annotation_label.appendChild(folder_label)

    filename_label = dom.createElement("filename")
    filename_text = dom.createTextNode(img_name)
    filename_label.appendChild(filename_text)
    annotation_label.appendChild(filename_label)

    path_label = dom.createElement("path")
    path_text = dom.createTextNode(img_path)
    path_label.appendChild(path_text)
    annotation_label.appendChild(path_label)

    source_label = dom.createElement("source")
    database_label = dom.createElement("database")
    database_text = dom.createTextNode("Unknown")
    database_label.appendChild(database_text)
    source_label.appendChild(database_label)
    annotation_label.appendChild(source_label)

    size_label = dom.createElement("size")
    width_label = dom.createElement("width")
    width_text = dom.createTextNode(str(img_shape[0]))
    height_label = dom.createElement("height")
    height_text = dom.createTextNode(str(img_shape[1]))
    if is_filp:
        width_label.appendChild(height_text)
        height_label.appendChild(width_text)
    else:
        width_label.appendChild(width_text)
        height_label.appendChild(height_text)
    depth_label = dom.createElement("depth")
    depth_text = dom.createTextNode(str(img_shape[2]))
    depth_label.appendChild(depth_text)
    size_label.appendChild(width_label)
    size_label.appendChild(height_label)
    size_label.appendChild(depth_label)
    annotation_label.appendChild(size_label)

    segmented_label = dom.createElement("segmented")
    segmented_text = dom.createTextNode(str(0))
    segmented_label.appendChild(segmented_text)
    annotation_label.appendChild(segmented_label)

    for object_label in object_list:
        annotation_label.appendChild(object_label)

    dom.appendChild(annotation_label)
    return dom


if __name__ == '__main__':
    # 切割图片储存路径
    save_img_dir = os.path.join(root_path, save_img_dir_name)
    if not os.path.exists(save_img_dir):
        os.makedirs(save_img_dir)
    # 切割标签储存路径
    save_ano_dir = os.path.join(root_path, save_ano_dir_name)
    if not os.path.exists(save_ano_dir):
        os.makedirs(save_ano_dir)

    # 切割比例
    w_rate = 4
    h_rate = 4

    #读取图片列表
    img_name_ls = read_img_list(src_img_dir)
    # 图片命名id格式化长度
    format_size = len(str(w_rate * h_rate))

    # 遍历图片
    for img_name in img_name_ls:
        # 图片路径
        img_path = os.path.join(src_img_dir, img_name)
        img_base_name = FileProcessor.getBaseName(img_name)
        # 标签路径
        annotation_name = img_base_name + ".xml"
        annotation_path = os.path.join(src_annotation_dir, annotation_name)

        # 读取object标签
        label_list = get_label_list(annotation_path)

        # 读图
        img = cv2.imread(img_path)
        print(img.shape)

        # 计算切割区域
        area_list = count_cut_area(w_rate, h_rate, img.shape)

        # 判断读入图片与标签记录长宽是否翻转
        label_list = get_label_list(annotation_path)
        ano_shape = get_anotation_shape(annotation_path)
        flip = check_flip(img.shape, ano_shape)

        # 遍历切割区域
        i = 0
        for area in area_list:
            id_str = str(i).zfill(format_size)
            # 切割后标签路径
            cut_ano_name = img_base_name + "_" + id_str + ".xml"
            cut_ano_path = os.path.join((save_ano_dir), cut_ano_name)

            # 获取切割区域内object标签
            cut_label_list = cut_annotation_scale(area, label_list, flip)

            # 当有切割区域内标签时，才输出
            if len(cut_label_list) > 0:
                # 切割后图片路径
                cut_img_name = img_base_name + "_" + id_str + ".jpg"
                cut_img_path = os.path.join(save_img_dir, cut_img_name)

                # 切割图片
                cut_img = cut_img_scale(area, img)
                cv2.imwrite(cut_img_path, cut_img)
                print(cut_img_path)

                # 生成标签
                dom = generate_annotation(cut_label_list, cut_img_name, cut_img_path, flip, cut_img.shape)
                dealXML.writeXML(cut_ano_path, dom)
                print(cut_ano_path)

                i = i + 1
    pass


