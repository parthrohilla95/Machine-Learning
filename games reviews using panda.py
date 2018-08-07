import numpy as np
import pandas as pd
data=pd.read_csv("C:\\Users\\user\\Downloads\\ign.csv")
x=[]
xbox=data.iloc[:,4]
year=data.iloc[:,8]
count=0
m=[]
j=[]
y=[]
k=[]
l=[]
for i in range(len(xbox)):
    x.append(xbox[i])   
for i in range(len(year)):
    y.append(year[i])

for i in range(len(xbox)):
    if((year[i]==2012)and(xbox[i]=='Xbox One')):
        m.append(year[i])
        a=len(m)
    if((year[i]==2013)and(xbox[i]=='Xbox One')):
        m.append(year[i])
        b=len(m)
    if((year[i]==2014)and(xbox[i]=='Xbox One')):
        m.append(year[i])
        c=len(m)
    if((year[i]==2015)and(xbox[i]=='Xbox One')):
        m.append(year[i])
        d=len(m)
    if((year[i]==2016)and(xbox[i]=='Xbox One')):
        m.append(year[i])
        e=len(m)
        
for i in range(len(xbox)):
    if((year[i]==2012)and(xbox[i]=='PlayStation 4')):
        k.append(year[i])
        f=len(k)
    if((year[i]==2013)and(xbox[i]=='PlayStation 4')):
        k.append(year[i])
        g=len(k)
    if((year[i]==2014)and(xbox[i]=='PlayStation 4')):
        k.append(year[i])
        h=len(k)
    if((year[i]==2015)and(xbox[i]=='PlayStation 4')):
        k.append(year[i])
        p=len(k)
    if((year[i]==2016)and(xbox[i]=='PlayStation 4')):
        k.append(year[i])
        z=len(k)

for i in range(len(xbox)):
    if((year[i]==2012)and(xbox[i]=='PC')):
        l.append(year[i])
        q=len(l)
    if((year[i]==2013)and(xbox[i]=='PC')):
        l.append(year[i])
        r=len(l)
    if((year[i]==2014)and(xbox[i]=='PC')):
        l.append(year[i])
        s=len(l)
    if((year[i]==2015)and(xbox[i]=='PC')):
        l.append(year[i])
        t=len(l)
    if((year[i]==2016)and(xbox[i]=='PC')):
        l.append(year[i])
        u=len(l)
row=['2012','2013','2014','2015','2016']
col=['xbox one','playstation 4','PC']
val=np.array([[0,f,q],[b,g,r],[c,h,s],[d,p,t],[e,z,u]])
new=pd.DataFrame(val,index=row,columns=col)
print(new)
