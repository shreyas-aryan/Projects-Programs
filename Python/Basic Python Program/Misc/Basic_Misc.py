#Variables--------------------------------------------------------------------------
first="shreyas"
last="aryan"
grade='A'
percent=87.2
rank=2
passed=True
if passed:
    print(f"{first} {last} has passed with grade {grade}, {percent}% and {rank}nd rank")
else:
    print(f"u failed, so no details to be provided for {first} {last}")

#Oddeven---------------------------------------------------------------------------
a=int(input("Enter a value to check if it's Odd or Even: "))
if a%2==0:
    print(f"Number {a} is Even")
else:
    print(f"Number {a} is Odd")

#+ve,0,-ve-------------------------------------------------------------------------
a=int(input("Enter a value: "))
if a>=0:
    if a==0:
        print(f"{a} is a Zero Value")
    else:
        print(f"{a} is a +ve value")
else:
    print(f"{a} is a -ve value")

#Rectangle peri, area----------------------------------------------------------------
a=float(input("Enter Length: "))
b=float(input("Enter Breadth: "))
area=a*b
peri=2*(a+b)
print(f"The Perimeter of length {a} and breadth {b} rectangle is {peri}")
print(f"The Area of length {a} and breadth {b} rectangle is {area}")

#factorial---------------------------------------------------------------------------
a=int(input("Enter value for factorial: "))
fact=1
for i in range(2,a+1):
    fact=fact*i
print(f"{fact}")

#n number's table---------------------------------------------------------------------
a=int(input("Enter the number for it's table: "))
for i in range(1,11):
    print(f"{a} * {i} = {a*i}")

#simple interest----------------------------------------------------------------------
a=float(input("Enter Principle amt: "))
b=float(input("Enter Rate of interest(in percent): "))
c=float(input("Enter Time(in yrs): "))
si=(a*b*c)/100
print(f"Principle: {a}")
print(f"Rate: {b:.2f}")
print(f"Time: {c:.2f}")
print(f"Simple interest: {si:.2f}")
amt=a+si
print(f"TOTAL AMOUNT: {amt:.2f}")

#compount interest--------------------------------------------------------------------
a=float(input("Enter Principle amt: "))
b=float(input("Enter Rate of interest(in percent): "))
c=float(input("Enter Time(in yrs): "))
print(f"Principle: {a}")
print(f"Rate: {b:.2f}")
print(f"Time: {c:.2f}")
amt=a*((1+(b/100))**c)
ci=amt-a
print(f"Compound interest: {ci:.2f}")
print(f"TOTAL AMOUNT: {amt:.2f}")

#circumference and area of circle-----------------------------------------------------
import math
r=float(input("Enter radius: "))
cir=2*math.pi*r
area=math.pi*(r**2)
print(f"Circumference {cir:.2f} and Area {area:.2f} of circle with radius {r:.2f}")

#hypotenouse of a triangle-----------------------------------------------------------
#sqrt(a**2+b**2)
import math
a=float(input("Enter side A: "))
b=float(input("Enter side B: "))
h=math.sqrt((a**2)+(b**2))
print(f"Side C: {h} Side A: {a} Side B: {b}")

#OPERATORS-------------------------------------------------------------------------
print("Shreyas Aryan-00521402024")
a=int(input("Enter Value: "))
b=int(input("Enter 2nd Value: "))
#arithmetic operations
print(f"\nARITHMETIC OPERATIONS")
print(f"{a} + {b} (sum) = {a+b}")
print(f"{a} - {b} (difference) = {a-b}")
print(f"{a} * {b} (multiplication) = {a*b}")
print(f"{a} / {b} (division) = {a/b}")
print(f"{a} ** {b} (exponent) = {a**b}")
print(f"{a} // {b} (floor division) = {a//b}")
print(f"{a} % {b} (modules) = {a%b}")
#comparison operations
print(f"\nCOMPARISON OPERATIONS")
print(f"{a} >= {b} = {a>=b}")
print(f"{a} != {b} = {a!=b}")
print(f"{a} < {b} = {a<b}")
#bitwise operations
print(f"\nBITWISE OPERATIONS")
print(f"{a} << {b} (left shift) = {a<<b}")
print(f"{a} >> {b} (right shift) = {a>>b}")
print(f"~{a} (not) = {~a}")
print(f"{a} & {b} (and) = {a&b}")
print(f"{a} | {b} (or) = {a|b}")
print(f"{a} ^ {b} (xor) = {a^b}")
#assignment operations
print(f"\nASSIGNMENT OPERATIONS")
a**=b
print(f"Value of A after a**=b: {a}")
a%=b
print(f"Value of A after a%=b: {a}")
a//=b
print(f"Value of A after a//=b: {a}")

#weight converting----------------------------------------------------------
print("Weight Convertor")
print("1.KGS to LBS")
print("2.LBS to KGS")
n=int(input("Enter your choice (1/2): "))
if n==1:
    kg=int(input("Enter weight in KGS: "))
    lb=kg*2.25
    print(f"{kg}kgs into lbs is {round(lb,3)}lbs")
elif n==2:
    lb=int(input("Enter weight in LBS: "))
    kg=lb/2.25
    print(f"{lb}lbs into kgs is {round(kg,3)}kgs")
else:
    print("INVALID OPTION!")

#temp converting--------------------------------------------------------------
print("Temp Convertor")
print("1.C to F")
print("2.F to C")
n=int(input("Enter your choice (1/2): "))
if n==1:
    c=int(input("Enter in Celcius: "))
    f=(c*(9/5))+32
    print(f"{round(c,2)}C converts into {round(f,2)}F")
elif n==2:
    f=int(input("Enter in Farenheit: "))
    c=(f-32)*(5/9)
    print(f"{round(f,2)}F converts into {round(c,2)}C")
else:
    print("INVALID OPTION!")

#ternary operator-------------------------------------------------------------
z=int(input("Enter value: "))
y=int(input("Enter 2nd value: "))
print("1st Value is greater" if z>y else "2nd Value is greater")
b=False
b=int(b)
a="hello" if b==1 else "no hello"
print(a)
num=5
print("positive" if num>=0 else "negative")
x=6
y=7
print("max x" if x>y else "max y")
print("min x" if x<y else "min y")
age=12
print("kid" if x<18 else "adult")
temp=48
print("hot" if temp>20 else "cold")
user="guest"
print("full access" if user=="admin" else "limited access")

#break at 10 sum of it--------------------------------------------------------
n=int(input("Enter value for nothing: "))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
    if i==10:
        break
print(sum)

#MINIMUM NUMBER---------------------------------------------------------------
a=13
b=23
c=2
print(f"{a}:A\t{b}:B\t{c}:C")
if a<b:
    if a<c:
        min=a
    else:
       min=c
else:
    if b<c:
        min=b
    else:
        min=c
print(f"{min} is the Minimum Number")

#type casting-------------------------------------------------------------------
str1=input("Enter String: ")
int1=int(input("Enter Integer: "))
flo1=float(input("Enter Float: "))
bool1=bool(input("Enter Boolean: "))
print("Type of int1: ",type(int1)," ",int1)
int1=str(int1)
print("Type of int1: ",type(int1)," ",int1)
print("Type of flo1: ",type(flo1)," ",flo1)
flo1=int(flo1)
print("Type of flo1: ",type(flo1)," ",flo1)
print("Type of bool1: ",type(bool1)," ",bool1)
bool1=str(bool1)
print("Type of bool1: ",type(bool1)," ",bool1)

#use of global keyword------------------------------------------------------------
x=10
y=20
def add():
    c=x+y
    print(c)
add()
def add2():
    global x,y
    x+=y
    print(x)
add2()

