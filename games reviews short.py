import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\user\\Downloads\\ign.csv")
platform=['Xbox One','PlayStation 4','PC']
years=np.array([2012,2013,2014,2015,2016])
val=np.zeros((15))
count=0
for i in range(len(platform)):
    for j in range(len(years)):
        val[count]=(np.count_nonzero((data['platform']==platform[i])& (data['release_year']==years[j])))
        count=count+1

val=(val.reshape(5,3))
val=val.astype(int)
d=pd.DataFrame(val,row=years,columns=platform)
plt.figure(1)
plt.plot(years,val[:,0],'g')
plt.plot(years,val[:,1],'r')
plt.plot(years,val[:,2],'b')
plt.show()


