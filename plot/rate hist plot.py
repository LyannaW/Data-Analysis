import matplotlib.pyplot as plt
x=[1,2,3]
y=[0.06,0.0076,0]
c=0.0297
plt.bar(x,y,color="skyblue",tick_label=['pacifier','hair dryer','microwave'])
plt.xlabel("Product",fontsize=15)
plt.ylabel("Rate of Repeated Purchasers",fontsize=15)
plt.title("Rate of Repeated Purchasers",fontsize=15)
plt.axhline(y=c,color="steelblue",linestyle='--',label='overall rate level')
plt.legend(loc='upper right')
plt.savefig('Rate of Repeated Purchasers.png')
plt.show()