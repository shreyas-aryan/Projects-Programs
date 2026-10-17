import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
y=[12,34,67,3,2,12,59,86]
x=["a","b","c",'d','e','f',"g",'h']
z=[78,98,67,56,86,76,56,78]
plt.xlabel("names")
plt.ylabel("marks")
plt.title("Students")
plt.grid(True,ls=":",lw=1)
plt.plot(x,y,c="r",ls="--",lw=1,marker="+",mec="y",mfc="b",ms=10,label="line")
plt.plot(x,z,c="g",ls=":",lw=3,marker="*",mec="b",mfc="y",ms=10)
plt.legend(["Sec A","Sec B"])
plt.show()
plt.scatter(x,y,c="r",marker=">",ec="g",label="scatter")
plt.show()
plt.bar(x,y,color="y",ec="g",lw=2,hatch="//",label="barh")
plt.show()
s=["red","green","blue","yellow","black","purple","pink","orange"]
plt.pie(y,labels=x,autopct="%1.2f%%",explode=[.1,0,0,0,0,.05,0,0],colors=s,shadow=True,startangle=90)
plt.show()
plt.hist(y,bins=30,color='red',ec="black")
plt.show()
a=np.random.randint(1,100,1000)
df=pd.DataFrame(a)
print(a.mean())
print(df.median())
print(df)
print(df.groupby(0)[0].count())
d=pd.pivot_table(df,index=0,values=0,aggfunc="count")
print(d)
plt.boxplot(a)
plt.show()
sns.kdeplot(df,color="red")
plt.show()
sns.histplot(df,bins=12, color="yellow")
plt.show()
sns.histplot(df, bins=30, kde=True, color='lightgreen', edgecolor='red')
plt.show()
