#use of static in python----------------------------------------------------------------
class Employee:
    sal=20
    def __init__(self,name,position):
        self.name=name
        self.position=position
        Employee.sal+=20
    def get_info(self):
        print(f"{self.name}={self.position}")
    @staticmethod
    def is_valid(pos):
        valid=["cook","manager","scientist"]
        print(pos in valid)
print(Employee.sal)
Employee.is_valid("cook")
c1=Employee("Shreyas","cook")
c2=Employee("Reyas","manager")
print(Employee.sal)
print(c2.sal)

#use of args and kwargs---------------------------------------------------------------
def a(*args,**kwargs):
    for i in args:
        print(i,end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs['street']} {kwargs['apt']}")
    elif "pobox" in kwargs:
        print(f"{kwargs['street']} {kwargs['pobox']}")
    else:
        print(f"{kwargs['street']}")
    print(f"{kwargs['city']} {kwargs['country']}")

a("Shreyas","Aryan",47,
  street="123 Faker",
  pobox="PO BOX #1001",
  #apt=100,
  city="Delhi",
  country="India")

#fibonacci---------------------------------------------------------------------------
n=int(input("enter the number of terms: "))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    a,b=b,a+b

#reverse of a number--------------------------------------------------------------------
n=int(input("enter the no: "))
rev=0
temp=n
while temp>0:
    d=temp%10
    rev=rev*10+d
    temp=temp//10
print(rev)

#linear search in list, and list operations-----------------------------------------------
print("LIST OF INTEGERS")
n=int(input("Enter the number of elements: "))
a=[]
for i in range(0,n,1):
    elem=int(input(f"Enter {i+1} Element: "))
    a.append(elem)
print("The User Inputted list is: ")
for i in a:
    print(i, end=" ")
print()
print("DELETED THE LAST ELEMENT")
a.pop()
a.sort(reverse=True)
for i in range(0,n-1,1):
    print(a[i], end=" ")
print()
sea=int(input("Enter the element to be found: "))
f=0
for i in a:
    if i==sea:
        f+=1
        print("Element found using list loop")
        break
for i in range(0,n,1):
    if a[i]==sea:
        f+=1
        print(f"Element found at Index {i} using range normal loop")
        break
if f==0:
    print("Element not found!")

#Armstrong---------------------------------------------------------------------------
a=int(input("enter a number: "))
temp=a
sum=0
n=len(str(a))
while temp>0:
    d=temp%10
    sum=sum+(d**n)
    temp=temp//10
if sum==a:
    print(a,"is an armstrong number")
else:
    print(a,"is not an armstrong number")

#checking username requriments--------------------------------------------------------
print("Username check!!")
n=input("Enter your Username: ")
if len(n)>12:
    print("Username cant contain more than 12 characters")
elif not n.isalpha():
    print("Username shouldnt have numbers")
elif not n.find(" ")==-1:
    print("Username cant have spaces")
else:
    print(f"Welcome {n}")
