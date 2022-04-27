import numpy as np
import cv2
import os

# path
path = r"D:\Mitek\GAN train\black region\origin data\CFD-AF-200-228-N.png"
destination_path=r"D:\Mitek\GAN train\black region\black_data"
image=cv2.imread(path)
dimension=image.shape

width=dimension[0]
height=dimension[1]

y_coord=width//4
x_coord=height//4
file_name=name=os.path.basename(path)
name_of_file=file_name[0:file_name.find(".")]
name_of_file_black=name_of_file+"_black.png"
print(f'file name is {file_name}---name of file {name_of_file}--- name of file black {name_of_file_black}')
join_path=os.path.join(destination_path,name_of_file_black)
print(join_path)
# iteration=20
# for _ in range(iteration):
#     image=cv2.imread(path)
#     x=np.random.randint(0,0.75*width)
#     y=np.random.randint(0,0.75*width)
#     l_1=x+np.random.randint(0.25*width,0.4*width)
#     l_2=y+np.random.randint(0.25*height,0.4*height)
#     print(f'x={x} y={y} l_1={l_1} l_2={l_2}')
#     cv2.rectangle(image, (x, y), (l_1, l_2), (0, 0, 0), -1)
#     cv2.imshow("image", image)
#     cv2.imwrite("image")
#     cv2.waitKey(0)
# # x=20
# # y=20
# # w=40
# # h=40

