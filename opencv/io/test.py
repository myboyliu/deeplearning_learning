# -*- coding: utf-8 -*-
import cv2
import numpy
import os
# numpy

py_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(os.path.dirname(py_dir))

img_test_path=project_dir+'/data_public/test.jpeg'
img_test2_path=project_dir+'/data_public/test2.jpeg'

print("project_dir:",project_dir)

img = numpy.zeros((3,3),dtype=numpy.uint8)
print(img)
print(img.shape)



#转换为BGR图片
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print(img)


img = cv2.imread(img_test_path)
cv2.imwrite(img_test2_path,img)
