import matplotlib.pyplot as plt
from sklearn import svm,metrics
import numpy as np
count1=0
tr_target=np.zeros((280))
tr_data=np.zeros((280,1178))
for i in range(1,41):
    for j in range(1,8):
        img='D:\\face recognition date base\\orl_face\\u'+str(i)+'\\'+str(j)+'.png'
        img=plt.imread(img)
        xpad=np.zeros((2,92))
        ypad=np.zeros((114,1))
        new_img=np.concatenate((img,xpad),axis=0)
        new_img=np.concatenate((new_img,ypad),axis=1)
        f=[]
        lb=[]
        k=''
        feature=np.zeros((1178))
        for row in range(0,114,3):
            for col in range(0,93,3):
                f=new_img[row:row+3,col:col+3]
                #print(f)
                c=f[1,1]
                for m in range(len(f)):
                    for n in range(len(f)):
                        if(c>=f[m,n]):
                            f[m,n]=1
                        elif(c<=f[m,n]):
                            f[m,n]=0
                f=f.astype(int)
                #print(f)
                k=k+str(f[0][1])
                k=k+str(f[0][0])
                k=k+str(f[1][0])
                k=k+str(f[2][0])
                k=k+str(f[2][1])
                k=k+str(f[2][2])
                k=k+str(f[1][2])
                k=k+str(f[0][2])
                k=k+str(',')
        k=k.split(',')
        count=0
        for m in range(1178):
            feature[count]=int(k[m],2)
            count=count+1
        
        tr_data[count1,:]=feature
        tr_target[count1]=i
        count1=count1+1      


count1=0
ts_target=np.zeros((120))
ts_data=np.zeros((120,1178))
for i in range(1,41):
    for j in range(8,11):
        img='D:\\face recognition date base\\orl_face\\u'+str(i)+'\\'+str(j)+'.png'
        img=plt.imread(img)
        xpad=np.zeros((2,92))
        ypad=np.zeros((114,1))
        new_img=np.concatenate((img,xpad),axis=0)
        new_img=np.concatenate((new_img,ypad),axis=1)
        f=[]
        lb=[]
        k=''
        feature=np.zeros((1178))
        for row in range(0,114,3):
            for col in range(0,93,3):
                f=new_img[row:row+3,col:col+3]
                #print(f)
                c=f[1,1]
                for m in range(len(f)):
                    for n in range(len(f)):
                        if(c>=f[m,n]):
                            f[m,n]=1
                        elif(c<=f[m,n]):
                            f[m,n]=0
                f=f.astype(int)
                #print(f)
                k=k+str(f[0][1])
                k=k+str(f[0][0])
                k=k+str(f[1][0])
                k=k+str(f[2][0])
                k=k+str(f[2][1])
                k=k+str(f[2][2])
                k=k+str(f[1][2])
                k=k+str(f[0][2])
                k=k+str(',')
        k=k.split(',')
        count=0
        for m in range(1178):
            feature[count]=int(k[m],2)
            count=count+1
        
        ts_data[count1,:]=feature
        ts_target[count1]=i
        count1=count1+1                                  
                
model=svm.SVC(kernel='linear',gamma=0.05)
d=model.fit(tr_data,tr_target)
out=d.predict(ts_data)
print(metrics.accuracy_score(out,ts_target))
