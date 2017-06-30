#!/usr/bin/env python3
#-*-encoding:utf-8-*-
#planA 通过长宽比例切出对应内容的图片
import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np
#处理横竖问题
def box_all(src_path,target_dir):
    if os.path.exists(src_path):
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        im = Image.open(src_path)
        #img = cv2.imread(src_path);
        box_cardno(im, target_dir)
        box_engineno(im, target_dir)
        box_vin(im, target_dir)





def box_cardno(im,target_dir):
    width = im.size[0]
    height = im.size[1]
    x =0
    y =height*0.26
    w = width*0.12
    h = height*0.32
    filename = "cardno_pre"
    box(x,y,w,h,im,target_dir,filename)
    x = width*0.14
    w = width * 0.47
    y = height * 0.29
    h = height * 0.34
    filename = "cardno"
    box(x, y, w, h, im, target_dir, filename)


def box_engineno(im,target_dir,nopre=0,filename='engineno'):
    pass


def box_vin(im,target_dir,nopre=0,filename='engineno'):
    pass



def box(x,y,w,h,im,target_dir,filename):
    target_path=target_dir + '/' + filename + '.jpg'
    if os.path.exists(target_path):
        os.remove(target_path)
    box = (x, y, w, h)
    region = im.crop(box)
    #region.show()
    region.save(target_path)
    return target_path






