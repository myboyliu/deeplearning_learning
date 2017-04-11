#!/usr/bin/env python3
#-*-encoding:utf-8-*-

import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np
#将图片设置为宽度必须等于width的图片


def resize(src_path,out_path,width):
    print("src_path:"+src_path)
    if os.path.exists(src_path):
        img = cv2.imread(src_path)
        img_height = img.shape[0]
        img_width = img.shape[1]
        print("width:",img_width)
        print("height:",img_height)
        img = cv2.resize(img, (width, round(width*0.7)), interpolation=cv2.INTER_CUBIC)
        print(out_path)
        out_dir_path = os.path.dirname(out_path)
        print(out_dir_path)
        if not os.path.exists(out_dir_path) :
            os.makedirs(out_dir_path)
        cv2.imwrite(out_path,img)
