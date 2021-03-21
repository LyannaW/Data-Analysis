# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:42:05 2020

@author: think
"""
import numpy as np
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
data_info=pd.read_csv('worst_ones.csv')
word_counts = dict(zip(data_info['word'],data_info['rating']))
mask = np.array(Image.open('bad.png'))  # word cloud background  
wc = wordcloud.WordCloud(
    background_color="white",
    font_path='C:/Windows/Fonts/Georgia.ttf',  # font
    mask=mask,  # picture background
    max_words=150,  # maximum number of words that we show
    max_font_size=150  
).generate_from_frequencies(word_counts)  # generate word cloud from dictionary

wc.to_file("new.jpg")  # save the picture
plt.imshow(wc)  # show the word cloud
plt.axis('off')  # close axis
plt.show()  # show the picture