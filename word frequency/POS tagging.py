# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 08:53:57 2020

@author: think
"""
import nltk
text_list=[]
tag=[]
import csv
with open('word_frequency_result.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        text_list.append(i[0])
        print(i[0])
i=0
while i <291:#lenth of text_list
    print(nltk.pos_tag(text_list,tagset='universal')[i])
    i+=1