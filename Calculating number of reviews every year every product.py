#!/usr/bin/env python
# coding: utf-8

# In[1]:


#calculate the number of reviews every year every product
import pandas as pd
import numpy as np


# In[17]:


hairdryer=pd.read_csv('hair_dryer_final_UTF8.tsv', sep='\t')
temp1 = hairdryer.loc[:,['product_parent','verified_purchase','year']]
result = temp1.groupby( ["product_parent","year"]).count()
result = pd.DataFrame(result)
result = result.unstack()
result = result.fillna(0)
result=result.astype(int)
result['product sales'] = result.apply(sum,axis=1)
result.loc['annual sales'] = result.apply(lambda x: x.sum())
result=result.sort_values(by='product sales',ascending=False)
result.to_excel('./hairdryer_sen.xlsx')


# In[18]:


microwave=pd.read_csv('microwave_final_UTF8.tsv', sep='\t')
temp1 = microwave.loc[:,['product_parent','verified_purchase','year']]
result = temp1.groupby( ["product_parent","year"]).count()
result = pd.DataFrame(result)
result = result.unstack()
result = result.fillna(0)
result=result.astype(int)
result['product sales'] = result.apply(sum,axis=1)
result.loc['annual sales'] = result.apply(lambda x: x.sum())
result=result.sort_values(by='product sales',ascending=False)
result.to_excel('./microwave_sen.xlsx')


# In[2]:


pacifier=pd.read_csv('pacifier_final_UTF8.tsv', sep='\t')
temp1 = pacifier.loc[:,['product_parent','verified_purchase','year']]
result = temp1.groupby( ["product_parent","year"]).count()
result = pd.DataFrame(result)
result = result.unstack()
result = result.fillna(0)
result=result.astype(int)
result['product sales'] = result.apply(sum,axis=1)
result.loc['annual sales'] = result.apply(lambda x: x.sum())
result=result.sort_values(by='product sales',ascending=False)
result.to_excel('./pacifier_sen.xlsx')

