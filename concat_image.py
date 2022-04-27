import cv2 
from os import listdir
from os.path import isfile,join
import os
import numpy as np


src_path=r"D:\Mitek\GAN train\black region\origin data"
des_path=r"D:\Mitek\GAN train\black region\black_data"

src_file=[f for f in listdir(src_path) if isfile(join(src_path,f))]
des_file=[f for f in listdir(des_path) if isfile(join(des_path,f))]

concat_path=r"D:\Mitek\GAN train\black region\concat data"
print(f"check={len(src_file)==len(des_file)}")
n=len(src_file)
for i in range(0,n):
    src_file_dir=src_path+"\\"+src_file[i]
    des_file_dir=des_path+"\\"+des_file[i]
    src_img=cv2.imread(src_file_dir)
    des_img=cv2.imread(des_file_dir)
    # cv2.imshow("src_img",src_img)
    # cv2.imshow("des_img",des_img)
    # cv2.waitKey(0)
    concat_img=cv2.hconcat([des_img,src_img])
    file_name=src_file[i][0:src_file[i].find(".")]+"_gan.png"
    concat_destion_path=os.path.join(concat_path,file_name)
    cv2.imwrite(concat_destion_path,concat_img)

