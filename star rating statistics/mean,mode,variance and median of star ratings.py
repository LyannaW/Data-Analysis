import pandas as pd
import numpy as np
df=pd.read_csv('pacifier_final.tsv',sep='\t')#change the path when applying to the other two datasets
df_group = df.groupby(by = 'product_parent')
Cata_list = list(df_group.groups.keys())#group by product_parent
df_groupnum = df.groupby(['product_parent']).size()#number of reviews
df_var=df.groupby(by = 'product_parent').star_rating.var()
df_mean=df.groupby(by = 'product_parent').star_rating.mean()
df_median=df.groupby(by = 'product_parent').star_rating.median()
##mode calculation
t1 = df.groupby([ 'product_parent', 'star_rating']).size().reset_index()
t1.columns = [ 'product_parent', 'star_rating', 'count']
t2 = t1.groupby([ 'product_parent'])['count'].max().reset_index()#Number of occurrences
t2.columns = [ 'product_parent', 'max_count']
t1 = t1.merge(t2, on=[ 'product_parent'], how='left')
t1 = t1[t1['count']==t1['max_count']]
t1 = t1.groupby([ 'product_parent'])['star_rating'].mean().reset_index()
##for vine voices
vine = df.groupby(['product_parent', 'vine']).size().reset_index()
vine_groupnum = df.groupby(['product_parent','vine']).size()#number of reviews for each product
vine_var = df['star_rating'].astype(float).groupby([df['product_parent'],df['vine']]).var()
vine_mean = df['star_rating'].astype(float).groupby([df['product_parent'],df['vine']]).mean()
vine_median = df['star_rating'].astype(float).groupby([df['product_parent'],df['vine']]).median()
vine_most=df['star_rating'].astype(float).groupby([df['product_parent'],df['vine']]).agg(lambda x: np.mean(x.mode())).reset_index()
##print to csv
df_print=pd.DataFrame(columns=())#empty dataframe
df_print["variance"]=df_var
df_print["mean"]=df_mean
df_print["groupnum"]=df_groupnum
df_print["median"]=df_median
df_print=pd.merge(df_print,t1,on = ['product_parent'])
df_print.to_csv("data_pacifier.csv",index=True,sep=',')
vine_print=pd.DataFrame(columns=())
vine_print['vine_variance']=vine_var
vine_print['vine_mean']=vine_mean
vine_print['vine_groupnum']=vine_groupnum
vine_print['vine_median']=vine_median
vine_most.to_csv('vine_most.csv',index=False,sep=',')
vine_print.to_csv("vine_data_pacifier.csv",index=True,sep=',')