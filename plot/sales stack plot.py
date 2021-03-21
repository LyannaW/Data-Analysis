import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.grid()
plt.rcParams['font.sans-serif'] = 'Consolas'
plt.rcParams['axes.unicode_minus'] = True
plt.rcParams['savefig.dpi'] = 1000
plt.style.use('ggplot')
sales=pd.read_excel('sale.xlsx')
labels = sales.index
print(labels)
channel = sales.columns
N = np.arange(sales.shape[0])
y1=sales[channel[1]]/14.0
y2=sales[channel[2]]/14.0
y3=sales[channel[3]]/14.0
colors = ['#75bbfd','#01386a','#2976bb']
plt.stackplot(N, y1,y2,y3,colors=colors)
for i in range(len(colors)):
	plt.plot([],[],color=colors[i],label=channel[i + 1],linewidth=5)
    
plt.legend(loc='upper left')
plt.title('2002-2015 Accumulated Sales of Three Products Market')
plt.ylabel('Accumulated Sales')
plt.xlabel('Year')
plt.xticks(N,sales[channel[0]].values)
plt.savefig('Stack_plot.png')
plt.show()
print(sales.columns)