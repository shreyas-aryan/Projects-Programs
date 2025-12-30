#matplotlib usage
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(6,4),facecolor='lightblue')
x=["a","b","c","d","e","f"]
y=[2,3,4,56,12,4]
b=[32,43,2,3,5,6]
plt.title("bullshit data")
plt.xlabel("students")
plt.ylabel("marks")
#plt.pie(y,labels=x,colors=("red","blue","pink","green","yellow","purple"),explode=(.3,.4,.2,0,0,0),shadow=True,autopct='%1.2f%%')
#plt.barh(x,y,color="red",edgecolor="black")
ax1=plt.subplot2grid((7,1),(0,0),rowspan=2,colspan=1)
ax2=plt.subplot2grid((7,1),(2,0),rowspan=2,colspan=1)
ax1.plot(x,y,color="red",linewidth=2,linestyle="--",marker="o", markersize=15)
ax2.plot(x,b)
plt.legend(labels=('l1','l2'))
plt.show()
