# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:41:39 2020

@author: think
"""


 # In[1] 
#Part I: analyze the types of products purchased by the same user (baby, beauty, major appliances)
#Note: in Excel, the data sets are sorted according to the customer_ID from small to large
import pandas as pd
df=pd.read_csv('repeated_ones_with_date_for_sales.csv')
i=0
num=0#Number of purchasers who purchase multiple products
man=0#Used to count the number of purchasers
while i<df.shape[0]:
    if (i==0):
        temp_category=df['product_category'][0]
        temp_id=df['customer_id'][0]
        judge=0#bool:judge=1 means a customer has bought more than one product
        man=1
    else:
        if(df['customer_id'][i]==temp_id):
            if(df['product_category'][i]!=temp_category):
                judge=1
        else:
            temp_category=df['product_category'][i]
            temp_id=df['customer_id'][i]
            if(judge==1):
                num+=1
            man+=1
            judge=0
    i+=1

 # In[2] 
#Part II: analyze the situation of users purchasing the same product
#Note: in Excel, the data sets are sorted by customer ID from small to large. For the same customer ID, the data sets are sorted by product parent from small to large
import pandas as pd

df=pd.read_csv('repeated_ones_with_date_for_sales.csv')
i=0
num=0#Number of purchasers who purchase the same ID product in the same category
man=0#Used to count the number of purchasers

df_size=df.groupby('customer_id').size()#get the number of each purchasers' reviews
while i<df.shape[0]:
    if (i==0):
        temp_id=df['customer_id'][0]
        temp_product=df['product_parent'][0]
        judge=0#0 means that IDs of the products purchased by the customer are different
        man=1
    else:
        if(df['customer_id'][i]==temp_id):
            if (df['product_parent'][i] == temp_product):
                judge=1
        else:
            temp_id=df['customer_id'][i]
            temp_product=df['product_parent'][i]
            if(judge==1):
                num+=1
            man+=1
            judge=0
    i+=1
 # In[3] 
#Part III: analyze the situation of repeated purchase of pacifiers in a short period of time among the users who purchase pacifiers
#Note that in Excel, the customer ID is sorted from small to large. For the same customer ID, the review date is used to sort from far to near
import pandas as pd
data=pd.read_csv('pacifier_repeated_ones_with_date_for_sales.csv')
data_size=data.groupby('customer_id').size()#Count the number of comments per user

i=0
num=0
while i< data.shape[0]:
    if (i==0):
        temp_id=data['customer_id'][0]
        temp_year=data['year'][0]
        temp_month=data['month'][0]
        temp_day=data['day'][0]
        judge=0#1 means the customer purchase products with the same category many times
    else:
        if(data['customer_id'][i]==temp_id):
            if data['year'][i]==temp_year and  data['month'][i]==temp_month and  data['day'][i]==temp_day:
                judge=1
        else:
            temp_id=data['customer_id'][i]
            temp_year=data['year'][i]
            temp_month=data['month'][i]
            temp_day=data['day'][i]
            if(judge==1):
                num+=1
            judge=0
    i+=1








