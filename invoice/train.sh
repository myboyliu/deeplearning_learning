#!/bin/sh

filepath=$(cd "$(dirname "$0")";cd ../; pwd)		#父级目录

train_img_dir=$filepath'/data/invoice/img/'
train_img_file='00247780-8553-7b63-d8b1-n202a134b354/box/1/cardno_pre.jpg'
train_img_file_path=$train_img_dir$train_img_file
echo 'training:'$train_img_file_path
train_dir=$filepath'/data/invoice/train/'

train_file_name='invoice.normal.exp0'

train_file_name_jpg=$train_file_name'.jpg'

train_file_name_tif=$train_file_name'.tif'
train_file_name_box=$train_file_name'.box'
train_file_name_tr=$train_file_name'.tr'

test_python_path=$filepath'/invoice/test.py'


tesseract_test_data_dir='/usr/local/Cellar/tesseract/3.05.00/share/tessdata/'

#复制到目标目录
cp -f $train_img_file_path $train_dir$train_file_name_jpg



#进入训练目录
cd $train_dir
#转换图片为tif文件和box文件,如有了则不重新生成了
if [ ! -f "$train_file_name_box" ];then
	convert -compress none -depth 8 -alpha off $train_file_name_jpg  $train_file_name_tif
	tesseract  $train_file_name_jpg $train_file_name  -l chi_sim batch.nochop makebox
fi

#数据训练
tesseract  $train_file_name_jpg $train_file_name  nobatch box.train
unicharset_extractor $train_file_name_box
if [ ! -f "font_properties" ];then
	echo "" >font_properties
fi
shapeclustering -F font_properties -U unicharset $train_file_name_tr
mftraining -F font_properties -U unicharset -O unicharset $train_file_name_tr
cntraining $train_file_name_tr

mv -f inttemp normal.inttemp
mv -f normproto normal.normproto
mv -f pffmtable normal.pffmtable
mv -f shapetable normal.shapetable
mv -f unicharset normal.unicharset

combine_tessdata normal.

cp -f $train_dir/normal.traineddata $tesseract_test_data_dir



/usr/local/bin/tesseract $train_img_file_path $train_img_dir/temp.txt -l chi_sim

#python3 $test_python_path
