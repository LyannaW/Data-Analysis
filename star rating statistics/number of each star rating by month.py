# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:19:46 2020

@author: think
"""
#%%split date and save to files
import pandas as pd
import numpy as np

df=pd.read_csv('pacifier_repeated_ones.csv')#change the path when applying to other dataset

data=df['review_date']
x = data.str.split("/")
i=0
j=0

x_new=np.zeros((df.shape[0],3),dtype=np.int)
while i<df.shape[0]:
    while j<3:
        x_new[i][j]=x[i][j]
        j+=1
    if j==3:
        j=0
    i+=1
    
x_new = pd.DataFrame(x_new,columns=['month','day','year'])
df['day']=x_new['day']
df['month']=x_new['month']
df['year']=x_new['year']
df.to_csv("pacifier_1.csv",index=False,sep=',')

#%%number of each star rating by month
import pandas as pd
import numpy as np
df=pd.read_csv('pacifier_1.csv')
star=np.zeros((80, 8), dtype=np.int)
temp_year=0
temp_month=0
i=0#for each row in df
j=-1#for each row in star,and one row stand for the number of star rating in one month
while i<df.shape[0]:
    if df['year'][i]==temp_year and df['month'][i]==temp_month:
        star[j][df['star_rating'][i]-1]+=1
        star[j][5]=df['year'][i]
        star[j][6]=df['month'][i]
        star[j][7]+=1
        i+=1
    else:
        j+=1
        star[j][df['star_rating'][i]-1]+=1
        star[j][5]=df['year'][i]
        star[j][6]=df['month'][i]
        star[j][7]+=1
        temp_year=df['year'][i]
        temp_month=df['month'][i]
        i+=1
pd_data = pd.DataFrame(star,columns=['one star','two stars','three stars','four stars',
                                     'five stars','year','month','groupnum'])
pd_data.to_csv('stars_pacifier_1.csv',index=False,sep=',')