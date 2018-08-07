import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\user\\Downloads\\ign.csv")
years=[2012,2013,2014,2015,2016]

##d={'year':years,'xbox':[0,0,0,0,0],'ps4':[0,0,0,0,0],'pc':[0,0,0,0,0]}
##for i in range(len(years)):
##    for j in range(len(data['release_year'])):
##        if(years[i]==data['release_year'][j]) and (data['platform'][j]=='Xbox One'):
##            d['xbox'][i]=d['xbox'][i]+1
##        if(years[i]==data['release_year'][j]) and (data['platform'][j]=='PlayStation 4'):
##            d['ps4'][i]=d['ps4'][i]+1
##        if(years[i]==data['release_year'][j]) and (data['platform'][j]=='PC'):
##            d['pc'][i]=d['pc'][i]+1
##
##
##d=pd.DataFrame(d)
##print(d)
##plt.figure(1)
##plt.plot(d['year'],d['xbox'],'r',label='xbox')
##plt.plot(d['year'],d['ps4'],'g',label='ps4')
##plt.plot(d['year'],d['pc'],'b',label='pc')
##plt.legend()
##plt.show()

score=['Amazing','Great','Good','Bad']        
f={'score':score,'ps3':[0,0,0,0],'pc':[0,0,0,0]}

for i in range(len(score)):
    for j in range(len(data['platform'])):
        if(score[i]==data['score_phrase'][j]) and (data['platform'][j]=='PlayStation 3'):
            f['ps3'][i]=f['ps3'][i]+1
        if(score[i]==data['score_phrase'][j]) and (data['platform'][j]=='PC'):
            f['pc'][i]=f['pc'][i]+1
            
f['ps3'][0]=(f['ps3'][0]/1804)*100
f['ps3'][1]=(f['ps3'][1]/4773)*100
f['ps3'][2]=(f['ps3'][2]/4741)*100
f['ps3'][3]=(f['ps3'][3]/1259)*100


f['pc'][0]=(f['pc'][0]/1804)*100
f['pc'][1]=(f['pc'][1]/4773)*100
f['pc'][2]=(f['pc'][2]/4741)*100
f['pc'][3]=(f['pc'][3]/1259)*100

f=pd.DataFrame(f)    
print(f)
index = np.arange(4)
bar_width =0.35
plt.figure(2)
plt.bar(index,f['pc'] , bar_width,color='b',label='pc') 
plt.bar(index + bar_width,f['ps3'], bar_width,color='g',label='ps3')
plt.xticks(index+0.17,score)
plt.xlabel('Score')
plt.ylabel('platform')
plt.legend() 
plt.show()

