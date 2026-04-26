#datframe
#numpy
#dict-<<<<<<<<<<<<<<<<<<IMP
#dict of lists
#lists of dict
#csv
#list
#nested list
#series
#dict of series
import pandas as pd
import numpy as np
d1=pd.DataFrame([[1,2,3,4,5],[23,45,34,22,22]])#df
print(d1)
d2=pd.DataFrame([[1,2,3,4,5],[23,45,34]],index=["Shreyas","aryan"],columns=["a","b","c","d","e"])#w index and cols
print(d2)
arr1=np.arange(1,10,1).reshape(3,3)#numpy
d3=pd.DataFrame(arr1)
print(d3)
di={1:"Traf",2:"sdsd",3:"esssdddd"}#dict iondex=0
d4=pd.DataFrame(di,index=[0])
print(d4)
di1={1:["ttrucik","asdsfd",0],
    2:["car","scooty","keys"],
    3:["sdsds",0,0],
    4:["cat",0,0]}
d5=pd.DataFrame(di1)#dol
print(d5)
c=pd.read_csv("C:/Users/Shreyas/Downloads/AQI_Data_ 2022.csv")#csv
d6=pd.DataFrame(c)
print(d6)
l1=[12,3,4,6,7]
d7=pd.DataFrame(l1)#list
print(d7)
l2=[12,34,[34,54,6],32,43]#nested list
print("-======================================================================================================================")
d8=pd.DataFrame(l2)
print(d8)
s1=pd.Series([12,3243,345,53,56])#series
d9=pd.DataFrame(s1)
print(d9)
lod=[{1:"Traf",2:"sdsd",3:"esssdddd"},{1:"Traf",2:"sdsd",3:"esssdddd"},{1:"Traf",2:"sdsd",3:"esssdddd"}]#lod
d10=pd.DataFrame(lod)
print(d10)
s2=pd.Series([10,20,40,30,40])
di3={"a":s2,"b":s2,"c":s2,"d":s2}#dos
d11=pd.DataFrame(di3)
print(d11)

print("\n")
print(d2)
print()
#IMPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
print(d2.loc["aryan"])#key names, access row
print(d2.iloc[1])#acces rows
print(d2["c"])#access cols
print(d2[["c","b"]])#access cols
d2["f"]=[1,2]#adding columns
d2.loc["ssd"]=[1,2,3,4,5,6]#adding rows
print(d2)
d2['a']=[4,5,7]#modify cols
d2.iloc[2]=[7,8,9,0,0,8]#modify rows
print(d2)
df=d2.drop("ssd",axis=0)#delete row
print(df)
df1=d2.drop("a",axis=1)#delete col
print(df1)
del d2["a"]#delete col
print(d2)

#agg funcs
print("\n")
print(d2)
print()
print(d2.describe())
d2.info()
print(d2["b"].min())
print(d2["b"].max())
print(d2["b"].count())
print(d2["b"].sum())
print(d2["b"].quantile(.75))
print(d2["b"].std())
print(d2["b"].var())
print(d2[["b","c","d"]].var())
print(d2["b"].mean())
print(d2["b"].mode())
print(d2["b"].median())
print(d2.count())


print("\n")
print(d2)
print()
d2=d2.rename(index={"aryan":"Aryan","ssd":"Weevil"},columns={"b":"a","c":"b","d":"c","e":"d","f":"e"})#NO INDEXES
print(d2)
d2=d2.sort_values("b",ascending=True)#sort columns
print(d2)
d2=d2.sort_index(ascending=False)#sort index
print(d2)
d2=pd.pivot_table(d2,values="b",index="c",aggfunc="sum")#c ke basis pe b aarha hai
print(d2)
print("\n")
print(d6)
print()
grp=d6.groupby("Month in 2022")#grouping
print(grp["Good Days"].mean())
print(grp["Bad days"].mean())
print(grp["Good Days"].median())#agg funcs
print("\n")
print(grp["Good Days"].sum())
print("SAME AS:")
pt=pd.pivot_table(d6,index="Month in 2022",values="Good Days",aggfunc="sum")
print(f"{pt}")
print(d2.describe())
d2.info()
p2=pd.pivot(d6,index="Month in 2022",columns="City",values="Good Days")
print(p2)

