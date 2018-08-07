import matplotlib.pyplot as plt
import numpy as np
a=10*np.random.random(1000)
a=a.reshape(500,2)


b=np.random.randint(25)
c=np.random.randint(25)
centroid1=a[b]
centroid2=a[c]
plt.figure(1)
plt.scatter(a[:,0],a[:,1])
plt.scatter(centroid1[0],centroid1[1])
plt.scatter(centroid2[0],centroid2[1])
plt.show()
f=(centroid1[0]+centroid2[0])/2
group1=[]
group2=[]
d=np.zeros((len(a)))

for i in range(len(a)):
    d[i]=a[i,0]
    if(d[i]>=f):
        group1.append(i)
    else:
        group2.append(i)

y=np.zeros((len(group1),2))
z=np.zeros((len(group2),2))
for i in range(len(group1)):
    y[i,:]=a[group1[i]]
    
for i in range(len(group2)):
    z[i,:]=a[group2[i]]
plt.figure(2)
plt.scatter(y[:,0],y[:,1])
plt.scatter(z[:,0],z[:,1])
plt.show()
