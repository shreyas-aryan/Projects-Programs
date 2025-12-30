#testing numpy-----------------------------------------------------------------
import numpy as np
a=np.array([1, 2, 3])
b=np.array([[1,2,3,4],[5,6,7,8]])
c=np.arange(1,11,1)
d=np.linspace(0,10,3)
e=np.zeros(4)
f=np.ones(7)
g=np.identity(5)
p=np.zeros(5,int)
print(p)
print(a,"\n")
print(b,"\n")
print(c,"\n")
print(d,"\n")
print(e,"\n")
print(f,"\n")
print(g,"\n")
h=np.array([9,8,7,6,5,4,3,4,2]).reshape(3,-1)
print(h,"\n")
print(a*2,"\n")
print(a**2,"\n")
print(a+2,"\n")
print(a>0,"\n")
print(a+d,"\n")
print(np.min(a),"\n")
print(np.max(a),"\n")
print(np.std(a),"\n")
print(np.var(a),"\n")
print(np.sum(a),"\n")
print(np.mean(a),"\n")
print(np.argmin(a),"\n")
print(np.argmax(a),"\n")
q=np.copy(a)
print(q)
print(np.dot(a,d))
p=(np.identity(3))+1
print(p)
print(np.dot(p,h))

#testing alnum vals----------------------------------------------------------------------------------------------------
n="shreyas"
n1="shreyas aryan"
n2="shreyasaryan"
n3="shreyas123"
n4="shreyas 123"
n5="123shreyas"
n6="123 shreyas"
n7="123"
n8="12 3"
n9="123s"
n0="12,3"
n11="sh,rey"
n12="sh,123"
print(n.isdigit())        
print(n1.isdigit())
print(n2.isdigit())
print(n3.isdigit())
print(n4.isdigit())
print(n5.isdigit())
print(n6.isdigit())
print(n7.isdigit())
print(n8.isdigit())
print(n9.isdigit())
print(n0.isdigit())
print(n11.isdigit())
print(n12.isdigit())
print("\n")
print(n.isalpha())        
print(n1.isalpha())
print(n2.isalpha())
print(n3.isalpha())
print(n4.isalpha())
print(n5.isalpha())
print(n6.isalpha())
print(n7.isalpha())
print(n8.isalpha())
print(n9.isalpha())
print(n0.isalpha())
print(n11.isalpha())
print(n12.isalpha())
print("\n")
print(n.isalnum())     
print(n1.isalnum())
print(n2.isalnum())
print(n3.isalnum())
print(n4.isalnum())
print(n5.isalnum())
print(n6.isalnum())
print(n7.isalnum())
print(n8.isalnum())
print(n9.isalnum())
print(n0.isalnum())
print(n11.isalnum())
print(n12.isalnum())

#testing lists------------------------------------------------------------------------------------
#built in stuff
print("LIST")
l1=[1,2,33,4,5]
l2=[65,64,2]
print(l1)
l1.append(6)
print(l1)
l1.insert(2,5)
print(l1)
l1.remove(1)
print(l1)
l1.pop()
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
print(l1.index(4))
l1.reverse()
print(l1)
l1.extend(l2)
print(l1)
print(l1.count(5))
l1.clear()
print(l1)
#max(l1), min(l2), any(l1), all(l1), len(l1), sum(l1), cmp(l1,l2), type(l1)

#sets---------------------------------------------------------------------------------------------------
print()
print("SETS")
s1={1,2,3,4,2,2,2,2,2,2,2,2,2,2,5,6}
print(s1)
s1.add(7)
print(s1)
s1.remove(2)
print(s1)
s1.pop()
print(s1)
print(len(s1))

#tuple---------------------------------------------------------------------------------------------------
print()
print("Tuples")
t1=(1,2,3,3,4,5)
#can take user input indirectly by taking input from list then converting it to a tuple
print(t1.index(3))
print(t1.count(3))
print(len(t1))

#dict------------------------------------------------------------------------------------------------------
print()
print("DICT")
n={1:"one",2:"two",3:"three",4:"four"}
print(n)
print(n[1])
print(n.get(1))
print(n.values())
for val in n.values():
    print(val,end=" ")
print()
print(n.keys())
for key in n.keys():
    print(key,end=" ")
print()
n.update({5:"five"})
print(n)
n.update({2:"three"})
print(n)
n.pop(3)
print(n)
n.popitem()
print(n)
print(n.items())
for key,val in n.items():
    print(f"{key}: {val}")
