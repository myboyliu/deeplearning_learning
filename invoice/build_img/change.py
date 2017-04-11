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




    mark_width_max= img_width/5
    mark_width_min= img_width/10
    mark_height_min=img_height/10
    mark_height_max = img_height/5
    img_new = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_new = cv2.adaptiveThreshold(img_new, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 10)
    image, cnts, hierarchy = cv2.findContours(img_new, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    print(len(cnts))
    #print(cnts)
    #build_img = cv2.cvtColor(build_img,cv2.COLOR_GRAY2BGR)
    mark=None
    area_map = {}
    for c in cnts:
        area = cv2.contourArea(c)
        area_map[area] = c
    sort_keys = sorted(area_map.keys())
    rect = area_map[sort_keys[-2]]
    print(rect)
    img_new = cv2.fillConvexPoly(img_new, rect, (0, 0, 0))
    cv2.imwrite(out_path, img_new)
    #img_new = cv2.cvtColor(img_new, cv2.COLOR_BGR2GRAY)
    img_new, cnts2, hierarchy = cv2.findContours(img_new, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    img_new = cv2.cvtColor(img_new, cv2.COLOR_GRAY2BGR)
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        area_map[area] = c
        #if area < 100000 :
        #    continue
        #cv2.drawContours(build_img, c, -1, (0, 255, 0), 10)
        #cv2.rectangle(build_img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        if w > mark_width_max:
            continue
        if  w <mark_width_min :
            continue
        if h > mark_height_max:
            continue
        if h <mark_height_min :
            continue
        if x> img_width- mark_width_max:
            continue
        #print(x,y,w,h)
        #print(area)
        #print(img_width*img_height)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        mark=c
    #cv2.imwrite(out_path,build_img)
    (x, y, w, h) = cv2.boundingRect(c)
    #print('why tb:',y+h,img_height)
    if y+h > img_height/2 and y+h<img_height:
        pts1 = np.float32([[0, 0], [img_width, img_height], [0, img_height]])
        pts2 = np.float32([[img_width, img_height], [0, 0], [img_width, 0]])
        M = cv2.getAffineTransform(pts1, pts2)
        img = cv2.warpAffine(img, M, (img_width, img_height))
    #cv2.imwrite(out_path, build_img)

