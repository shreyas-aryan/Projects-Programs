#series
#numpy
#dict
#dict of lists
#csv
#list
#nested list
import pandas as pd
import numpy as np
from scipy.stats import skew as sk
from scipy.stats import kurtosis as kurt
data = [10, 12, 12, 13, 12, 14, 16, 18, 19, 20, 22, 24, 25, 25, 28, 30, 30, 32]
ssd=pd.Series(data)
print(sk(ssd))
print(ssd.skew())
print(kurt(ssd))
print(ssd.kurt())
s1=pd.Series([12,34,56,78,56])#series
print(s1)
s2=pd.Series([12,34,56,78,56],index=[1,2,3,4,5])#w index
print(s2)
l1=[12,3,4,6,7]
s3=pd.Series(l1)#list
print(s3)
l2=[12,34,[34,54,6],32,43]#nested list
s4=pd.Series(l2)
print(s4)
arr=np.arange(1,10,2)#numpy
s5=pd.Series(arr)
print(s5)
d=pd.read_csv("C:/Users/Shreyas/Downloads/AQI_Data_ 2022.csv")#read_csv, mention column
s6=pd.Series(d["Good Days"])#IMPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
print(s6)
di={1:"ttrucik",2:"car",3:"sdsds",4:"cat"}#dict
s7=pd.Series(di)
print(s7)
d1={1:"ttrucik",
    2:["car","scooty","keys"],
    3:"sdsds",
    4:"cat"}
s8=pd.Series(d1)#dict of lists
print(s8)

print("\n")
print(s1)
print(s1.head())
print(s1.head(2))#first 2
print(s1.tail(2))#last 2
print(s1.head(0))#not index, empty
print(s1.head(-2))#last 2 ke alawa,every value expect last n values
print(s1.tail(-2))#phele 2 ke alawa,every value except starting n values
print(s1)#mathematical ops
print(s1+1)
print(s1*2)
print(s1-1)
print(s1/2)
print(s1**2)
print(s1%2)
print(s1//2)
