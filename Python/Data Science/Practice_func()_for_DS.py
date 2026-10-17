#list
#emp=[id,name,sal]
#creaion indexing
l1=[[0,1,2,3],["shreyas","aryan","reyas","weevil"],20000]
print(l1[2])#positive indexing
print(l1[1])
print(l1[1][0])
print(l1[0][3])
print()
print(l1[-1])#negative indexing
print(l1[-2])
print(l1[-2][-4])
print(l1[-3][-1])
print()
print(l1)
l1[2]=50000#updating
l1[0][-2]=4
print(l1)
print()
l1[0].append(2)#append-add value at end
l1[1].append("hijesh")
l1.append([19,20,18,23,22])
l1[1].insert(-3,["jj","opps","rrr"])#insert-add value at index
print(l1)
print()
del l1[1][-3]#remove value at index
l1[1][2].remove("rrr")#remove value of first occurance
print(l1[1][2].pop(0))#default last value, or index, returns deleted value
print(l1)

#tuples
t1=(0,"John",30000,"Failed")
t2=(1,"Shreyas",40000,"Passed")#creation
t3=(23,43,45,34,23)
print(t1[1])#indexing
print(t1[-3])
print()
print(t2[1:3])#slicing
print(t1[2:])
print(t1[1::2])
print(len(t1))#built in
print(max(t3))
print(min(t3))
t4=t1+t2+t3#concat
print(t4)

#dict
d1={1:"shreyas",2:"reyas",3:"Weevil",4:"Beewomp"}#creation
print()
print(d1[2])#indexing
print(d1.keys())
print(d1.values())
print(d1.items())
d1[1]="heee"#update
d1[6]="ssd"#adding
print(d1)
d1.update({1:"hhhhh",5:"shreyas"})#update and add
print(d1)
del d1[3]#delete from keys
print(d1)
d1.clear()#empty dict
print(d1)

#sets
s1={12,23,45,6,34}
s2={23,45,21,12,45}#creation
s1.add(50)#inserting
print(s1)
s1.discard(23)#removing
print(s1)
u=s1.union(s2)
print(u)
x=s1.intersection(s2)
print(x)
d=s1.difference(s2)
print(d)
ss=s1.symmetric_difference(s2)
print(ss)
s1.clear()#empty set
print(s1)
