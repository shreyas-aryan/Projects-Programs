# list,tuple,dict,set
# input,traverse,add,remove,search,sort

# list
l1=[]
n=int(input("ENTER SIZE OF int LIST: "))
for i in range(0,n):
    elem=int(input(f"Enter {i}th Element: "))
    l1.append(elem)
print("THE LIST using List traverse: ")
for i in l1:
    print(f"{i}",end= " ")
print("\nTHE LIST using Traverse: ")
for i in range(0,n):
    print(f"{l1[i]}",end=" ")
print("\nREMOVING ELEMENT: ")
l1.pop(1)
for i in l1:
    print(f"{i}",end= " ")
print("\nSEARCHING ELEMENT: ")
m=int(input("ENTER ELEMENT TO BE FOUND: "))
for i in range(0,(n-1)):
    if(l1[i]==m):
        print(f"ELEMENT {l1[i]} FOUND at index {i}")
        break
print("SORTING: ")
l1.sort(reverse=True)
for i in l1:
    print(f"{i}",end= " ")

# tuple
print("\n")
t1=tuple(l1)
print("\nTHE Tuple using tuple traverse: ")
for i in t1:
    print(i,end=" ")
print("\nTHE tuple using traverse: ")
for i in range(0,(len(t1))):
    print(f"{t1[i]}",end= " ")
print("\nSEARCHING ELEMENT: ")
m=int(input("ENTER ELEMENT TO BE FOUND: "))
for i in range(0,(len(t1))):
    if(t1[i]==m):
        print(f"ELEMENT {t1[i]} FOUND at index {i}")
        break

# set
print("\n")
s1=set()
n=int(input("ENTER SIZE OF int SET: "))
for i in range(0,n):
    elem=int(input("Enter Element: "))
    s1.add(elem)
print("THE SET using SET traverse: ")
for i in s1:
    print(f"{i}",end= " ")
print("\nREMOVING ELEMENT: ")
s1.pop()
for i in s1:
    print(f"{i}",end= " ")
print("\nSEARCHING ELEMENT: ")
m=int(input("ENTER ELEMENT TO BE FOUND: "))
for i in s1:
    if(i==m):
        print(f"ELEMENT {i} FOUND")
        break

# dictionary
print("\n")
d1={}
n=int(input("ENTER SIZE OF int Dict: "))
for i in range(0,n):
    key=input(f"Enter Key: ")
    value=input(f"Enter Value: ")
    d1[key]=value
print("THE Dict using dict traverse: ")
for k,v in d1.items():
    print(f"{k}: {v}",end= " ")
print("\nTHE Dict keys using dict traverse: ")
for k in d1.keys():
    print(f"{k}",end= " ")
print("\nTHE Dict values using dict traverse: ")
for v in d1.values():
    print(f"{v}",end= " ")
print("\nREMOVING ELEMENT: ")
d1.pop("USA")
for k,v in d1.items():
    print(f"{k}: {v}",end= " ")
print("\nSEARCHING Value: ")
m=input("ENTER VALUE TO BE FOUND: ")
for k,v in d1.items():
     if(v==m):
         print(f"ELEMENT {v} FOUND at key {k}")
         break
print("SORTING: ")
d1=dict(sorted(d1.items()))
for k,v in d1.items():
    print(f"{k}: {v}",end= " ")
