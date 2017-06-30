#!/usr/bin/env python3
#-*-encoding:utf-8-*-
#planA 通过长宽比例切出对应内容的图片
import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np
import invoice.build_img.box as box
import invoice.build_img.resize as resize
import shutil
#处理横竖问题
tesseract_exe_name = '/usr/local/bin/tesseract' # Name of executable to be called at command line
cleanup_scratch_flag = True  # Temporary files cleaned up after OCR operation

def text_all(file_path_box_dir,width):
    min_area=width*0.006*width*0.006*0.73
    max_area = width * 0.019 * width * 0.019 * 0.73
    print(min_area,max_area)
    if os.path.exists(file_path_box_dir):
        text_cardno(file_path_box_dir,min_area,max_area)
        pass

def text_cardno(file_path_box_dir,min_area,max_area):
    #首先解析是否是身份证表格
    pre_text_file=file_path_box_dir + '/1/cardno_pre.jpg'
    pre_text_array = text(pre_text_file, min_area, max_area)
    text_dir = pre_text_file + "_text"
    ##判断此区域内的图片包含'身'或者'份'字,即说明是正向,否则为反向
    index=0
    im = Image.open(pre_text_file)
    for c in pre_text_array:
        (x, y, w, h) = cv2.boundingRect(c)
        width = x + w
        height = y + h
        target_path = box.box(x, y, width, height, im, text_dir, str(index))
        resize.resize(target_path,target_path,28,28)
        index += 1
        text_str = get_text(target_path)
        print(text_str)

    #text(file_path_box_dir+'/1/cardno.jpg',min_area,max_area)

    #text(file_path_box_dir + '/2/cardno.jpg',min_area,max_area)
    #text(file_path_box_dir + '/2/cardno_pre.jpg', min_area, max_area)

def text(path_img,min_area,max_area):
    bulid_file_path=path_img+".build.jpg"
    bulid_check_file_path = path_img + ".buildcheck.jpg"
    img = cv2.imread(path_img, 0)  # 直接读为灰度图像
    dev = cv2.meanStdDev(img)
    print(dev)
    # avg_gray = dev[1][0][0]
    avg_gray_1 = dev[0][0][0]
    avg_gray_2 = dev[1][0][0]
    param1 = 45
    param2 = 3
    """
    if avg_gray_1 > 130 and avg_gray_1 < 140 and avg_gray_2 > 5 and avg_gray_2 < 10:
        #test_name.append("01413180-8590-ltkg-9n3f-n202a8t5h778")
        param1 = 53
        param2 = 4
    if avg_gray_1 > 185 and avg_gray_1 < 190 and avg_gray_2 > 15 and avg_gray_2 < 20:
        # test_name.append("09089630-6405-43cg-4l28-n204ag3t5dtk")
        param1 = 211
        param2 = 3
    if avg_gray_1 > 190 and avg_gray_1 < 200 and avg_gray_2 > 20 and avg_gray_2 < 25:
        # test_name.append("08027230-6441-ekf3-9c2f-n202ak1h7ftb")
        param1 = 99
        param2 = 2
    if avg_gray_1 > 200 and avg_gray_1 < 210 and avg_gray_2 > 15 and avg_gray_2 < 20:
        #test_name.append("07473840-6432-g32k-e814-n202allfgf71")
        param1 = 79
        param2 = 4
    if avg_gray_1 > 210 and avg_gray_1 < 220 and avg_gray_2 > 5 and avg_gray_2 < 10:
        #test_name.append("04290710-7933-d9kd-8e5e-n202akg45n4k")
        param1 = 59
        param2 = 6
    if avg_gray_1 > 210 and avg_gray_1 < 220 and avg_gray_2 > 15 and avg_gray_2 < 20:
        # test_name.append("03127720-8931-h26k-g81h-n203abddfkk1")
        param1 = 29
        param2 = 4
    if avg_gray_1 > 210 and avg_gray_1 < 220 and avg_gray_2 > 25 and avg_gray_2 < 30:
        #test_name.append("04255340-5743-gglh-elfd-n203a56b63d3")
        param1 = 29
        param2 = 4

    print(avg_gray_1, avg_gray_2)
    print(param1, param2)
    """

    newimg = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, param1, param2)
    cv2.imwrite(bulid_file_path, newimg)
    image, cnts, hierarchy = cv2.findContours(newimg, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    newimg2 = cv2.cvtColor(newimg,cv2.COLOR_GRAY2BGR)
    index=0
    im = Image.open(path_img)
    text_dir = path_img + "_text"
    text_dirb = path_img + "_textb"
    if os.path.exists(text_dir):
        shutil.rmtree(text_dir)

    if os.path.exists(text_dirb):
        shutil.rmtree(text_dirb)
    os.makedirs(text_dir)
    os.makedirs(text_dirb)
    min_x_y = 10000000
    max_x_y = -1
    max_x = -1
    max_y = -1

    LT_point = -1
    RB_point = -1
    RT_point = -1
    LB_point = -1
    result=[]
    for c in cnts:
        area = cv2.contourArea(c)
        if area < min_area or area> max_area:
            #cv2.drawContours(newimg, c, -1, (255, 255, 255), 3)
            continue
        result.append(c)
        #print(area,min_area,max_area)
        (x, y, w, h) = cv2.boundingRect(c)
        width = x+w
        height = y+h
        box.box(x, y, width, height, im, text_dir, str(index))
        index+=1
        newimg2 = cv2.rectangle(newimg2, (x, y), (x + w, y + h), (255, 0, 0), 2)
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


        #newimg = cv2.drawContours(newimg, c, 1, (0, 255, 0), 3)
    cv2.imwrite(bulid_check_file_path,newimg2)
    return result
    #Image.open(bulid_check_file_path).show()
    #get_text(path_img,bulid_check_file_path)



def get_text(path_img_src,lan='chi_sim'):
    param1 = 21
    param2 = 1
    bulid_file_path=path_img_src+'.bulid.jpg'
    img = cv2.imread(path_img_src,0)
    newimg = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, param1, param2)
    cv2.imwrite(bulid_file_path, newimg)
    proc = subprocess.Popen(tesseract_exe_name + ' ' + bulid_file_path + ' ' + path_img_src + ' -l '+lan, shell=True)
    retcode = proc.wait()
    print(retcode)
    if retcode != 0:
        print(retcode)
        # errors.check_for_errors()
    inf = open(path_img_src + '.txt', 'r')
    text = inf.read()
    print(text)
    inf.close()
    return text