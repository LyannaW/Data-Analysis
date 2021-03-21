#!/usr/bin/env python
# coding: utf-8

# In[1]:


#group the reviews of the product with the same product parent
import pandas as pd
hairdryer=pd.read_csv('hair_dryer_final_UTF8.tsv',sep='\t')
import numpy as np


# In[2]:


temp1 = hairdryer.loc[:,['product_parent','star_rating']]
review = hairdryer.loc[:,['product_parent','review_headline','review_body']]
review = review.sort_values(by='product_parent',ascending=False)


# In[3]:


result = temp1.groupby('product_parent').mean()


# In[4]:


number=temp1.groupby('product_parent').count()


# In[5]:


result=result.sort_values(by='product_parent',ascending=False)


# In[6]:


number=number.sort_values(by='product_parent',ascending=False)


# In[7]:


writer = pd.ExcelWriter('./hairdryer_mean.xlsx')
result.to_excel(writer,'sheet1')
number.to_excel(writer,'sheet2')
review.to_excel(writer,'sheet3')


# In[8]:


writer.save()

