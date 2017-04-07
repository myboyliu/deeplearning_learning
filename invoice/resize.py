#-*-encoding:utf-8-*-
import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np
#将图片设置为宽度必须等于width的图片
def resize(src_path,out_path,width):
    img = cv2.imread(src_path)
    print(img.width)
