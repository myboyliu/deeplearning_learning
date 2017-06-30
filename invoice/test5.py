#-*-encoding:utf-8-*-
import os,sys
from PIL import Image
import subprocess
import cv2
import numpy as np
import invoice.build_img.resize as resize
import invoice.build_img.data as data
import invoice.build_img.change as change
import invoice.build_img.check as check
import invoice.build_img.box as box
import invoice.build_img.text as text
#公共参数
py_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(py_dir)

img_file= project_dir+"/data/invoice/img.txt"

file_dir_img_root = project_dir+"/data/invoice/img/"

#读取图片列表
imgs = data.getimgs(img_file,file_dir_img_root)
test_name=[]
test_name.append("00247780-8553-7b63-d8b1-n202a134b354")
#test_name.append("01362710-8011-h74m-622d-n204afcc45mt")
#test_name.append("01399570-7852-63d2-1432-n203add75k4k")
#test_name.append("01413180-8590-ltkg-9n3f-n202a8t5h778")
#test_name.append("02476410-7970-fg12-b221-n202anglkg23")
#test_name.append("03127720-8931-h26k-g81h-n203abddfkk1")
#test_name.append("04255340-5743-gglh-elfd-n203a56b63d3")
#test_name.append("04290710-7933-d9kd-8e5e-n202akg45n4k")
#test_name.append("06528180-8579-edh2-5k73-n204a13678m5")
#test_name.append("06576180-8876-dfm1-khk8-n204a46k7e7d")
#test_name.append("07473840-6432-g32k-e814-n202allfgf71")
#test_name.append("08027230-6441-ekf3-9c2f-n202ak1h7ftb")
#test_name.append("09089630-6405-43cg-4l28-n204ag3t5dtk")

#.jpg
#.jpg
#.jpg
#.jpg
#09089630-6405-43cg-4l28-n204ag3t5dtk.jpg
#09171200-7098-kf8h-5f53-n204a35c9l6e.jpg
#10463430-8299-6dff-g8ct-n202allfn39b.jpg
#10592470-7744-bmnk-1475-n203afgtn9db.jpg
#11311840-4244-m6td-7hl7-n203a4edl67f.jpg
#11483590-7534-9ecb-l7ng-n204a4d5bk9b.jpg
#12322700-7846-9816-793m-n204ab8gtk3d.jpg
#13449390-8652-fdm2-4glg-n202a19kg94n.jpg
#13531660-8105-eg2g-6l22-n203a88d45lg.jpg
#13578120-6619-kt9b-8l4c-n204a16eb5m4.jpg
#14596130-7702-ceee-9et7-n202akf1bnml.jpg
#16037000-7590-d691-kl8t-n203ae76m5lk.jpg
#16049250-7843-egl6-6khh-n202ac9ke21b.jpg
#17272160-7352-b3fm-ng24-n202a5nf69bm.jpg
#20420020-6694-b6c8-fh3k-n202a3129kf8.jpg
#2068300-6609-gh1b-hcfm-n204a6n5142n.jpg
#22095360-8730-425b-2e1b-n204a2hbbkh1.jpg
#23409370-6656-cl3g-tn8t-n203a96c6h8l.jpg
#25595520-7799-lndt-mdem-n202a56m8l2g.jpg
#27176320-4758-dleg-76f8-n202at85m558.jpg
#27358660-6405-8hc3-4dkn-n203ad2h81eg.jpg
#28215270-6525-kt4t-gbnb-n204a3t47dtf.jpg
#28222200-6641-1chl-2e5c-n204akf35e3c.jpg
#28389320-6406-9f4f-e5f6-n203akh6hn3c.jpg
#29224330-7716-mggb-tdh1-n202abbe276m.jpg
#29279340-7526-tth7-b44f-n203a581fb9g.jpg
#29482730-7857-bktk-3det-n202aeg6tn86.jpg
#29519770-7675-68fe-c2eb-n202a1493d5n.jpg
#30032110-6409-7lm9-lft7-n204a495cee3.jpg
#30113330-7939-bfk5-38k5-n202abb7t6ck.jpg
#31476270-6772-4b13-bg4n-n204ad5cl8he.jpg
#32115380-7378-1bml-b6m1-n202atcfcedb.jpg
#32198650-8898-277k-8t33-n204at5994ll.jpg
#34107600-6480-tmme-5nlg-n203agmtcl3t.jpg
#34216670-5437-g2b9-ge3g-n204adgd4nh2.jpg
#35146140-7690-ntd5-7c7g-n202a812hdf7.jpg
#35462110-6824-7f33-d3kc-n202a1ke3e64.jpg
#35488950-8794-b5ck-tb28-n203akcb846n.jpg
#36130120-7881-fhht-6t44-n202akbc46c3.jpg
#36372250-8878-l592-b489-n204a1983eb8.jpg
#37154290-8632-nb3n-fnel-n204a3cmbmnn.jpg
#37307480-7698-t4c7-m4nc-n202a6l429e5.jpg
#38567250-6866-62tg-bl3b-n203a7cb6782.jpg
#39100190-7801-k6l5-hdg7-n202a8b7nken.jpg
#39408710-8416-4ddt-lf77-n202ahhc3h44.jpg
#40264890-6501-em2k-lnhl-n204a3h9h5k3.jpg
#40269450-6502-g9km-6ch5-n204a1llld6k.jpg
#41586520-7668-chbe-1gce-n204abm4cf7d.jpg
#42050500-7988-mh86-g686-n204ae9f7nem.jpg
#42083840-6399-kmn3-2118-n204a5ln9g9g.jpg
#42531470-6377-l5bl-5ee5-n204a1hml721.jpg
#43470400-8619-9fk3-e791-n204a44e91d2.jpg
#45354480-1970-f8fk-9lhh-n202afnmkk4c.jpg
#47010500-8692-73kk-64de-n202agg27ll7.jpg
#48049350-7428-37ed-7gh7-n204ahg3t79e.jpg
#48147250-7983-k9bd-4ee6-n203ac4fld9e.jpg
#48170320-6708-e88k-7m91-n202al1te382.jpg
#49294680-3055-12g3-bmkc-n203a7157529.jpg
#50079050-8559-7551-c7fm-n202an61k8dc.jpg
#50176580-7821-62m3-kne9-n202a45n4tgl.jpg
#50224790-6943-ghf6-kccl-n204adblcn73.jpg
#51026630-7828-3gln-7t8t-n204acc9ggel.jpg
#51293840-7829-1meb-1e17-n204abd3hl5m.jpg
#53476530-8388-n8dd-hc5k-n202aef659ek.jpg
#57068830-6439-1cld-e8h9-n202ae3dl58h.jpg
#59283550-8831-997m-9cl5-n203a31fh694.jpg
#59535310-3215-333n-fbd9-n204a6n6t3nd.jpg
#6229140-6623-h99k-nc92-n202acbde3hg.jpg
#9292580-6600-m3l7-nhc9-n202alkkl69m.jpg

width =2048
#test_name=None
exclude=[]

exclude.append('04005040-7417-41d5-be2d-n203a829dmge')# 边框问题
exclude.append('28222200-6641-1chl-2e5c-n204akf35e3c')# 边框问题
exclude.append('30032110-6409-7lm9-lft7-n204a495cee3')# 边框问题
exclude.append('39100190-7801-k6l5-hdg7-n202a8b7nken')# 边框问题
exclude.append("10592470-7744-bmnk-1475-n203afgtn9db")# 边框问题
exclude.append("06471570-7965-l9te-4l6d-n202acfhebnb")# 图片分辨率太低,至少大于800*600

for img in imgs:

    path = img["path"]
    file_name =img["name"]
    if file_name in exclude:
        continue
    file_suffix = img["suffix"]
    if (test_name ==None or file_name in test_name or len(test_name)==0) :
        # 原图
        file_path_src = file_dir_img_root + file_name + '.' + file_suffix
        file_path_src_copy = file_dir_img_root + file_name + '/src_copy'+file_name +'.'+ file_suffix
        # 横竖调整图
        file_path_change_wh = file_dir_img_root + file_name + '/change_wh'+file_name +'.' + file_suffix
        # 大小调整
        file_path_resize = file_dir_img_root + file_name + '/resize'+file_name +'.'+ file_suffix
        # 灰度二值图
        file_path_gray = file_dir_img_root + file_name + '/gray'+file_name +'.' + file_suffix
        # 上下调整图
        file_path_change_tb = file_dir_img_root + file_name + '/change_tb'+file_name +'.' + file_suffix
        # 检测发票表格图
        file_path_rect = file_dir_img_root + file_name + '/rect'+file_name +'.' + file_suffix

        file_path_box_dir = file_dir_img_root + file_name + '/box'

        cv2.imwrite(file_path_src_copy,cv2.imread(file_path_src))
        # 横竖处理
        change.change_wh(file_path_src,file_path_change_wh)

        #上下重置
        #change.change_tb(file_path_resize,file_path_change_tb)
        #矫正并抽出中心内容
        check.check_rect(file_path_change_wh,file_path_rect)
        # 大小重置
        resize.resize(file_path_rect,file_path_resize,width)

        change.change_tb(file_path_resize, file_path_change_tb)
        # 图片切割
        box.box_all(file_path_resize,file_path_box_dir+'/1')

        box.box_all(file_path_change_tb, file_path_box_dir+'/2')


        info = text.text_all(file_path_box_dir,width)
        print(info)













