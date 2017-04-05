#-*-encoding:utf-8-*-
import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np

py_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(py_dir)
myfile = project_dir+"/data/invoice/img/09089630-6405-43cg-4l28-n204ag3t5dtk.jpg"
newfile = project_dir+"/data/invoice/img/09089630-6405-43cg-4l28-n204ag3t5dtk_new.jpg"
newfile_dir = project_dir+"/data/invoice/img"
tesseract_exe_name = 'tesseract' # Name of executable to be called at command line
scratch_image_name = "temp.bmp" # This file must be .bmp or other Tesseract-compatible format
scratch_text_name_root = "temp" # Leave out the .txt extension
cleanup_scratch_flag = True  # Temporary files cleaned up after OCR operation

def image_to_scratch(im, scratch_image_name):
    im.save(scratch_image_name, dpi=(200,200))

def call_tesseract(input_filename, output_filename):
    """Calls external tesseract.exe on input file (restrictions on types),
    outputting output_filename+'txt'"""
    args = [tesseract_exe_name, input_filename, output_filename,'-l','chi_sim']
    #args = [tesseract_exe_name, input_filename, output_filename,'-l','normal']

    proc = subprocess.Popen(args)
    retcode = proc.wait()
#    if retcode!=0:
#        errors.check_for_errors()
def image_to_string(im, cleanup = cleanup_scratch_flag):
    """Converts im to file, applies tesseract, and fetches resulting text.
    If cleanup=True, delete scratch files after operation."""
    text=""
    try:
        image_to_scratch(im, scratch_image_name)
        call_tesseract(scratch_image_name, scratch_text_name_root)
        text =retrieve_text(scratch_text_name_root)
    finally:
        if cleanup:
            perform_cleanup(scratch_image_name, scratch_text_name_root)
    return text
def	retrieve_text(scratch_text_name_root):
    inf = open(scratch_text_name_root + '.txt','r')
    text = inf.read()
    inf.close()
    return text

def perform_cleanup(scratch_image_name, scratch_text_name_root):
    """Clean up temporary files from disk"""
    for name in (scratch_image_name, scratch_text_name_root + '.txt', "tesseract.log"):
        try:
            os.remove(name)
        except OSError:
            pass

# 二值化
threshold = 185
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)




im = Image.open(myfile)
pix = im.load()
width = im.size[0]
height = im.size[1]
#for x in range(width):
#    for y in range(height):
#        r, g, b = pix[x, y]
#        print(pix[x, y]);

#转化到灰度图
#im = im.convert("RGB")
im = im.convert('L')

#im=im.point(lambda i : i*1.3) #对每一个像素点进行增强

#im = im.point(table,'1')

#保存图像
#im.save(newfile)
print(im.size)
index_x = 0
index_y=0
width=500
height=500
box = (0, 0, width, height)
images = []
while index_x <im.size[0] :
    while index_y<im.size[1] :
        #print(index_x,index_y);
        #box = (index_x, index_y, index_x+width, index_y+height)
        #region = im.crop(box)
        #img_out_path=newfile_dir+'/%d_%d.jpg' % (index_x,index_y)

        #img = cv2.imread(img_out_path,0) #直接读为灰度图像
        #newimg= cv2.adaptiveThreshold(img , 100,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
        #region = Image.fromarray(newimg, None)
        #region.save(img_out_path)
        #im.paste(region, box)
        index_y+=height
    index_x+=width
    index_y=0
img = cv2.imread(myfile,0) #直接读为灰度图像
newimg= cv2.adaptiveThreshold(img , 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,77,10)
im = Image.fromarray(newimg, None)
im.save(newfile)



img = cv2.GaussianBlur(newimg,(3,3),0)
edges = cv2.Canny(img, 50, 150, 3)
lines = cv2.HoughLines(edges,1,np.pi/180,118)
result = img.copy()

#经验参数
minLineLength = 50
maxLineGap = 40
lines = cv2.HoughLinesP(edges,1,np.pi/360,50,minLineLength,maxLineGap)
print(len(lines))
index_line=0;
while index_line<len(lines) :
    for x1,y1,x2,y2 in lines[index_line]:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),20)
    index_line+=1;


im = Image.fromarray(img, None)
im.save(newfile)
#
#box = (0, 1000, 500, 1500)
#region = im.crop(box)
#region.show()
#region = region.transpose(Image.ROTATE_180)
#im.paste(region, box)
#im.show()
#
#out.save(newfile)
#text = image_to_string(im)
#print(text)