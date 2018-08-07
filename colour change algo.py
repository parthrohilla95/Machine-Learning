import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
img_path="C:\\Users\\user\\Desktop\\parrot.jpg"
img=cv2.imread(img_path)
a=np.copy(img[:,:,0])
img[:,:,0]=img[:,:,2]
img[:,:,2]=a
l=[]
l=img.shape
img=img.reshape((l[0]*l[1]),l[2])
k=KMeans()
d=k.fit(img)
out=d.predict(img)
#plt.scatter(img[:,0],img[:,1],img[:,2],c=out)
#plt.show()
#colour=d.predict([[255,255,255]])
color_cord=np.where(out==0)
img[color_cord[0],0]=0
img[color_cord[0],1]=0
img[color_cord[0],2]=255
color_cord=np.where(out==1)
img[color_cord[0],0]=255
img[color_cord[0],1]=0
img[color_cord[0],2]=0
color_cord=np.where(out==2)
img[color_cord[0],0]=255
img[color_cord[0],1]=255
img[color_cord[0],2]=0
color_cord=np.where(out==3)
img[color_cord[0],0]=255
img[color_cord[0],1]=0
img[color_cord[0],2]=255
color_cord=np.where(out==4)
img[color_cord[0],0]=0
img[color_cord[0],1]=255
img[color_cord[0],2]=255
color_cord=np.where(out==5)
img[color_cord[0],0]=0
img[color_cord[0],1]=255
img[color_cord[0],2]=0
color_cord=np.where(out==6)
img[color_cord[0],0]=0
img[color_cord[0],1]=0
img[color_cord[0],2]=255
color_cord=np.where(out==0)
img[color_cord[0],0]=0
img[color_cord[0],1]=0
img[color_cord[0],2]=0


img=img.reshape(l[0],l[1],l[2])
plt.imshow(img)
plt.show()
