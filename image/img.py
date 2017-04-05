import cv2
import os

py_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(py_dir)
myfile = project_dir+"/data/invoice/img/09089630-6405-43cg-4l28-n204ag3t5dtk.jpg"
newfile = project_dir+"/data/invoice/img/09089630-6405-43cg-4l28-n204ag3t5dtk_new.jpg"
img = cv2.imread(myfile)
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img)
cv2.imshow("grayImage", GrayImage)
cv2.waitKey(0)
cv2.destroyAllWindopws()