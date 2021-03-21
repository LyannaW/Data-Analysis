# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:12:02 2020

@author: think
"""
import pandas as pd
word_list=pd.read_csv('processed_tagged_data.csv')
data=pd.read_csv('all_review.tsv',sep='\t')
j=0
rating=[]
while j<word_list.shape[0]:
    counter=0
    temp=0
    i=0
    while i< data.shape[0]:
        if word_list['word'][j] in data['review_headline'][i] or word_list['word'][j] in data['review_body'][i]:
            temp+=data['star_rating'][i]
            counter+=1
        i+=1
    if (counter==0):
        rating.append(0)
    else:rating.append(temp/counter)
    j+=1
word_list['rating']=rating
word_list.to_csv('final_results.csv')