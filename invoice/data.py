#!/usr/bin/env python3
#-*-encoding:utf-8-*-

import os,sys
import re
from urllib import request
from PIL import Image
import subprocess
import cv2
import numpy as np
#处理横竖问题
def getimgs(img_file,targetpath):
    result=[]
    with open(img_file, 'r') as f:
        for line in f.readlines():
            imgurl=line.strip()
            re_str = '.*/(.*)\.(.*)'
            re_pat = re.compile(re_str)
            search_ret = re_pat.search(imgurl)
            if search_ret:
                #print(search_ret.groups())
                file_name =search_ret.groups()[0]
                file_suffix=search_ret.groups()[1]

                out_path=targetpath+'%s.%s' % (file_name,file_suffix)
                img={}
                img['name']=file_name
                img['suffix']=file_suffix
                img['path']=out_path
                if not os.path.exists(out_path):
                    try:
                        #print(out_path)
                        request.urlretrieve(imgurl, out_path)
                        result.append(img)
                    except Exception as err:
                        pass
                        #print(err)
                    finally:
                        pass
                else :
                    result.append(img)
    return result

