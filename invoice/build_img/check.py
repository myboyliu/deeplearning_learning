#!/usr/bin/env python3
#-*-encoding:utf-8-*-

import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np
#处理横竖问题
def check_rect(src_path,out_path):
    if os.path.exists(out_path):
        os.remove(out_path)
    out_dir_path = os.path.dirname(out_path)
    if not os.path.exists(out_dir_path) :
        os.makedirs(out_dir_path)
    print("src_path:"+src_path)
    print("out_path:"+out_path)
    img = cv2.imread(src_path)

    img_height = img.shape[0]
    img_width = img.shape[1]

    print("width:",img_width)
    print("height:",img_height)
    img_new = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dev = cv2.meanStdDev(img_new)
    print(dev)
    #avg_gray = dev[1][0][0]
    avg_gray_1 = dev[0][0][0]
    avg_gray_2 = dev[1][0][0]
    param1 = 11
    param2 = 3
    if avg_gray_1>100 and avg_gray_1 < 110 and  avg_gray_2 >40 and avg_gray_2 < 45:
        #test_name.append("22095360-8730-425b-2e1b-n204a2hbbkh1")
        param1 = 9
        param2=5
    if avg_gray_1 > 110 and avg_gray_1 < 120 and avg_gray_2 > 25 and avg_gray_2 < 30:
        #test_name.append("32115380-7378-1bml-b6m1-n202atcfcedb")
        param1 = 17
        param2 =3
    if avg_gray_1 > 110 and avg_gray_1 < 120 and avg_gray_2 > 55 and avg_gray_2 < 60:
        #test_name.append("41586520-7668-chbe-1gce-n204abm4cf7d")
        param1 = 19
        param2 = 3
    if avg_gray_1>120 and avg_gray_1 < 130 and  avg_gray_2 >25 and avg_gray_2 < 30:
        param1 = 13
        param2=3
    if avg_gray_1>120 and avg_gray_1 < 130 and  avg_gray_2 >35 and avg_gray_2 < 40:
        #test_name.append("17272160-7352-b3fm-ng24-n202a5nf69bm")
        param1 = 11
        param2=4
    if avg_gray_1 > 130 and avg_gray_1 < 140 and avg_gray_2 > 10 and avg_gray_2 < 15:
        #51293840-7829-1meb-1e17-n204abd3hl5l
        param1 = 99
        param2 = 3
    if avg_gray_1>150 and avg_gray_1 < 160 and  avg_gray_2 >20 and avg_gray_2 < 25:
        #test_name.append("28215270-6525-kt4t-gbnb-n204a3t47dtf")
        param1 = 33
        param2=3
    if avg_gray_1 > 150 and avg_gray_1 < 160 and avg_gray_2 > 25 and avg_gray_2 < 30:
        #51026630-7828-3gln-7t8t-n204acc9ggel
        param1 = 27
        param2 = 3
    if avg_gray_1 > 170 and avg_gray_1 < 180 and avg_gray_2 > 25 and avg_gray_2 < 30:
        #test_name.append("48049350-7428-37ed-7gh7-n204ahg3t79e")
        param1 = 11
        param2 = 5
    if avg_gray_1>170 and avg_gray_1 < 180 and  avg_gray_2 >40 and avg_gray_2 < 50:
        param1 = 11
        param2=5


    print(avg_gray_1,avg_gray_2)
    print(param1,param2)
    img_new = cv2.adaptiveThreshold(img_new, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, param1, param2)
    image, cnts, hierarchy = cv2.findContours(img_new, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    img_new = cv2.cvtColor(img_new, cv2.COLOR_GRAY2RGB)
    area_map = {}
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        area_map[area]=c
    sort_keys = sorted(area_map.keys())
    min_x_y = 10000000
    max_x_y = -1
    max_x = -1
    max_y = -1

    LT_point = -1
    RB_point = -1
    RT_point = -1
    LB_point = -1
    for i in range(-2, -1):
        c = area_map.get(sort_keys[i])
        for cc in c:
            # print(cc)
            x = cc[0][0]
            y = cc[0][1]
            if x + y < min_x_y:
                min_x_y = x + y
                LT_point = [x, y]
            if x + y > max_x_y:
                max_x_y = x + y
                RB_point = [x, y]
            if x - y > max_x:
                max_x = x - y
                RT_point = [x, y]
            if y - x > max_y:
                max_y = y - x
                LB_point = [x, y]

        img_new=cv2.drawContours(img_new, c, -1, (0, 255, 0), 10)

    print(LT_point, LB_point, RT_point, RB_point)
    if os.path.exists(out_path+'test.jpg'):
        os.remove(out_path+'test.jpg')
    cv2.imwrite(out_path+'test.jpg', img_new)
    height, width, channels = img.shape
    try:
        pts1 = np.float32([LT_point, RT_point, LB_point, RB_point])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        PerspectiveMatrix = cv2.getPerspectiveTransform(pts1, pts2)
        img = cv2.warpPerspective(img, PerspectiveMatrix, (width, height))
        cv2.imwrite(out_path, img)
    #except Exception as err:
    #    pass
    finally:
        pass




