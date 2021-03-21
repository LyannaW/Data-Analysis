# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:36:30 2020

@author: think
"""

import matplotlib.pyplot as plt
 
name_list = ['127431946','236392593','253917972','258419037','277493012','303775294',
             '464779766','486774008','591023894','635386699','692404913','732252283','768062995'     
]
num_list = [0,0.666666667,1.165501166,1.556507442,2.139784946,1.476811594,
            2.238095238,0.92124031,0.266666667,1.965465465,3.05,1.367192216,0.744708995,
            ]
num_list1 = [0.529166667,0.561904762,1.113636364,0.401098901,0.212418301,0.472727273,
             0.476190476,0.763636364,0.221052632,0.725274725,0.266666667,0.369281046,0.743589744,
]
plt.barh(range(len(num_list)), num_list,height=0.8, label='Normal Users',fc = 'lightskyblue')
plt.barh(range(len(num_list)), num_list1, height=0.6,label='Amazon Vine Voices',tick_label = name_list,fc = 'dodgerblue')
plt.xlabel('Variance')
plt.ylabel('Product Parent')
plt.legend()
plt.show()