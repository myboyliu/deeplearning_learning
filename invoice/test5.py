#-*-encoding:utf-8-*-
import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np
import invoice.build_img.resize as resize
import invoice.build_img.data as data
import invoice.build_img.change as change
import invoice.build_img.check as check
#公共参数
py_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(py_dir)

img_file= project_dir+"/data/invoice/img.txt"

file_dir_img_root = project_dir+"/data/invoice/img/"

#读取图片列表
imgs = data.getimgs(img_file,file_dir_img_root)
test_name=[]
test_name.append("01362710-8011-h74m-622d-n204afcc45mt")

#test_name=None
exclude=[]

exclude.append('04005040-7417-41d5-be2d-n203a829dmge')# 边框问题
exclude.append('28222200-6641-1chl-2e5c-n204akf35e3c')# 边框问题
exclude.append('30032110-6409-7lm9-lft7-n204a495cee3')# 边框问题
exclude.append('39100190-7801-k6l5-hdg7-n202a8b7nken')# 边框问题
exclude.append("10592470-7744-bmnk-1475-n203afgtn9db")# 边框问题

for img in imgs:

    path = img["path"]
    file_name =img["name"]
    if file_name in exclude:
        continue
    file_suffix = img["suffix"]
    if (test_name ==None or file_name in test_name or len(test_name)==0) :
        # 原图
        file_path_src = file_dir_img_root + file_name + '.' + file_suffix
        file_path_src_copy = file_dir_img_root + file_name + '/src_copy'+file_name +'.'+ file_suffix
        # 横竖调整图
        file_path_change_wh = file_dir_img_root + file_name + '/change_wh'+file_name +'.' + file_suffix
        # 大小调整
        file_path_resize = file_dir_img_root + file_name + '/resize'+file_name +'.'+ file_suffix
        # 灰度二值图
        file_path_gray = file_dir_img_root + file_name + '/gray'+file_name +'.' + file_suffix
        # 上下调整图
        file_path_change_tb = file_dir_img_root + file_name + '/change_tb'+file_name +'.' + file_suffix
        # 检测发票表格图
        file_path_rect = file_dir_img_root + file_name + '/rect'+file_name +'.' + file_suffix

        cv2.imwrite(file_path_src_copy,cv2.imread(file_path_src))
        # 横竖处理
        change.change_wh(file_path_src,file_path_change_wh)

        #上下重置
        #change.change_tb(file_path_resize,file_path_change_tb)
        #矫正并抽出中心内容
        check.check_rect(file_path_change_wh,file_path_rect)
        # 大小重置
        resize.resize(file_path_rect,file_path_resize,512)


        #图片切割













