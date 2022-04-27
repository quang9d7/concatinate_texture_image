import cv2 
from os import listdir
from os.path import isfile,join
import os
import numpy as np


src_path=r"D:\Mitek\GAN train\black region\origin data"
des_path=r"D:\Mitek\GAN train\black region\black_data"

all_file=[f for f in listdir(src_path) if isfile(join(src_path,f))]
num_file=len(all_file)
for file in all_file:
    print(file)
    file_dir=src_path+"\\"+file
    print(file_dir)
    image=cv2.imread(file_dir)
    dimension=image.shape
    width=dimension[0]
    height=dimension[1]
    y_coord=width//4
    x_coord=height//4
    x=np.random.randint(0,0.75*width)
    y=np.random.randint(0,0.75*width)
    l_1=x+np.random.randint(0.25*width,0.4*width)
    l_2=y+np.random.randint(0.25*height,0.4*height)
    print(f'x={x} y={y} l_1={l_1} l_2={l_2}')
    cv2.rectangle(image, (x, y), (l_1, l_2), (0, 0, 0), -1)
    
   
    file_name=file[0:file.find(".")]+"_black.png"
    destination_path=os.path.join(des_path,file_name)
    cv2.imwrite(destination_path,image)
  