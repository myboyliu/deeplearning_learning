#-*-encoding:utf-8-*-
import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np

py_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(py_dir)
#file_name='09089630-6405-43cg-4l28-n204ag3t5dtk'
file_name='tes1'
myfile = project_dir+"/data/invoice/img/"+file_name+".jpg"
#myfile = project_dir+"/data/invoice/img/111.jpg"
#二值化图片
newfile = project_dir+"/data/invoice/img/"+file_name+"_new.jpg"
#方格检测图片
my_file_1 = project_dir+"/data/invoice/img/"+file_name+"_new_1.jpg"
#图形矫正
my_file_2 = project_dir+"/data/invoice/img/"+file_name+"_new_2.jpg"
my_file_3 = project_dir+"/data/invoice/img/"+file_name+"_new_3.jpg"
newfile_dir = project_dir+"/data/invoice/img"


img = cv2.imread(myfile,0) #直接读为灰度图像
newimg= cv2.adaptiveThreshold(img , 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,10)
im = Image.fromarray(newimg, None)
im.save(newfile)
img = newimg
#
image, cnts, hierarchy = cv2.findContours(img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img= cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)


class Invoice(object):
    same_point_map={}
    same_point_area_map = {}
    same_point_num_max=0
    same_point_max=[]
    same_point__max_cnts=[]

    def same_point_process(self,point,c):
        (x, y, w, h) = point
        self.same_point_area_map[cv2.contourArea(c)]=c
        self.same_point_one_process(x,y,c,1,point)
        self.same_point_one_process(x+w, y,c,2,point)
        self.same_point_one_process(x, y+h,c,3,point)
        self.same_point_one_process(x+w, y + h,c,4,point)

    def same_point_one_process(self,x,y,c,l,point):
        same_key = str(l) + '_' + str(x)+'_'+str(y)
        same_point = self.same_point_map.get(same_key)
        if same_point == None:
            same_point =[]
        same_point_num = len(same_point)
        node ={}
        node['x']=point[0]
        node['y']=point[1]
        node['w']=point[2]
        node['h']=point[3]
        node['px'] = x
        node['py'] = y
        node['l']=l
        same_point.append(node)
        self.same_point_map[same_key]=same_point


invoice = Invoice()
for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)

    invoice.same_point_process((x, y, w, h),c)

#invoice.offset(1)
#print(invoice.same_point_area_map)
min_x_y=10000000
max_x_y=-1
max_x=-1
max_y=-1

LT_point=-1
RB_point=-1
RT_point=-1
LB_point=-1
sort_keys = sorted(invoice.same_point_area_map.keys())
for i in range(-2,-1) :
    c = invoice.same_point_area_map.get(sort_keys[i])
    #(x, y, w, h) = cv2.boundingRect(c)
    #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    for cc in c :
        #print(cc)
        x = cc[0][0]
        y = cc[0][1]
        if x+y < min_x_y:
            min_x_y =x+y
            LT_point=[x,y]
        if x+y > max_x_y:
            max_x_y = x+y
            RB_point = [x, y]
        if x-y >max_x:
            max_x =x-y
            RT_point=[x,y]
        if y-x > max_y:
            max_y = y-x
            LB_point = [x, y]

    cv2.drawContours(img, c, -1, (0, 255,0 ), 10)
    #print(sort_keys[i])

print(LT_point,LB_point,RT_point,RB_point)


def drawRect(img,point,size):
    x=point[0]
    y=point[1]
    w=size
    h=size
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

drawRect(img,LT_point,10)
drawRect(img,RB_point,10)
drawRect(img,RT_point,10)
drawRect(img,LB_point,10)
cv2.imwrite(my_file_2, img)




#矫正处理
height , width , channels = img.shape
pts1 = np.float32([LT_point, RT_point, LB_point,RB_point])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
PerspectiveMatrix = cv2.getPerspectiveTransform(pts1,pts2)
img = cv2.warpPerspective(img, PerspectiveMatrix, (width, height))
cv2.imwrite(my_file_3, img)

