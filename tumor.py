import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import cv2
f='c:\\Users\\user\\Downloads\\brain_image.jpg'
img=cv2.imread(f)
a=np.copy(img[:,:,0])
img[:,:,0]=img[:,:,2]
img[:,:,2]=a
l=[]
l=img.shape
img=img.reshape((l[0]*l[1]),l[2])
k=KMeans(3)
d=k.fit(img)
out=d.predict(img)
print(img)
color_cord=np.where(out==0)
img[color_cord[0],0]=0
img[color_cord[0],1]=0
img[color_cord[0],2]=0
color_cord=np.where(out==1)
img[color_cord[0],0]=255
img[color_cord[0],1]=255
img[color_cord[0],2]=255
color_cord=np.where(out==2)
img[color_cord[0],0]=0
img[color_cord[0],1]=0
img[color_cord[0],2]=0

img=img.reshape(l[0],l[1],l[2])
plt.imshow(img)
plt.show()

