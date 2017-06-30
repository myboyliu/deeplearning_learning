#!/usr/bin/env python3
#-*-encoding:utf-8-*-

import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np
#处理横竖问题
def change_wh(src_path,out_path):
    if os.path.exists(out_path):
        os.remove(out_path)
    out_dir_path = os.path.dirname(out_path)
    if not os.path.exists(out_dir_path) :
        os.makedirs(out_dir_path)
    #print("src_path:"+src_path)
    #print("out_path:"+out_path)
    img = cv2.imread(src_path)

    img_height = img.shape[0]
    img_width = img.shape[1]

    #print("width:",img_width)
    #print("height:",img_height)
#如果长宽比错误,进行90度的处理
    if img_height>img_width :
        #M = cv2.getRotationMatrix2D((img_height/2,img_width/2), 90, 1)
        pts1 = np.float32([[0, 0], [img_width, 0], [0, img_height]])
        pts2 = np.float32([[img_width, 0], [img_width, img_height], [0, 0]])
        M = cv2.getAffineTransform(pts1, pts2)
        img = cv2.warpAffine(img, M, (img_width,img_height))
        img = cv2.resize(img, (img_height,img_width ), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(out_path,img)

def change_tb(src_path,out_path):
    if os.path.exists(out_path):
        os.remove(out_path)
    out_dir_path = os.path.dirname(out_path)
    if not os.path.exists(out_dir_path):
        os.makedirs(out_dir_path)
    # 如果上线颠倒,进行180度的处理
    print("src_path:"+src_path)
    print("out_path:"+out_path)
    img = cv2.imread(src_path)

    img_height = img.shape[0]
    img_width = img.shape[1]

    print("width:",img_width)
    print("height:",img_height)
    pts1 = np.float32([[0, 0], [img_width, img_height], [0, img_height]])
    pts2 = np.float32([[img_width, img_height], [0, 0], [img_width, 0]])
    M = cv2.getAffineTransform(pts1, pts2)
    img = cv2.warpAffine(img, M, (img_width, img_height))
    cv2.imwrite(out_path, img)

