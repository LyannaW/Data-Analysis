#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
hairdryer=pd.read_csv('hair_dryer_final_UTF8.tsv', sep='\t')
import numpy as np


# In[2]:


hairdryer


# In[3]:


temp1 = hairdryer.loc[:,['product_parent','verified_purchase','year']]
temp1.head()#select to calculate


# In[4]:


result = temp1.groupby( ["year","product_parent"]).sum()
result.head()#calculate the number of verified purchase every kind of products every year


# In[5]:


result = pd.DataFrame(result)
result = result.unstack()
result = result.fillna(0)
result=result.astype(int)
result.head()#rearrange the table and fill 'NaN' with zero 


# In[6]:


result['annual sales'] = result.apply(sum,axis=1)
result
#annual sales of every product


# In[7]:


result.loc['product sales'] = result.apply(lambda x: x.sum())
result
#total product sales


# In[8]:


result.to_excel('./hairdryer_sales.xlsx')
#save the document

