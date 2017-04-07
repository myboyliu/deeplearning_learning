#-*-encoding:utf-8-*-
import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np
from . import resize
#公共参数
py_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(py_dir)

file_dir_img_root = project_dir+"/data/invoice/img"
file_name='tes1'
file_suffix='jpg'
#原图
file_path_src = file_dir_img_root+file_name+'.'+file_suffix
#大小调整
file_path_resize= file_dir_img_root+file_name+'/resize.'+file_suffix
#灰度二值图
file_path_gray= file_dir_img_root+file_name+'/gray.'+file_suffix
#检测发票表格图
file_path_rect= file_dir_img_root+file_name+'/rect.'+file_suffix
#方向调整图
file_path_change= file_dir_img_root+file_name+'/rect.'+file_suffix
#结果图
file_path_result= file_dir_img_root+file_name+'/result.'+file_suffix

