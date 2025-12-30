#calculator, ifs, loops, def
def add(n,m):
    print(f"{n} + {m} = {n+m}")

def sub(n,m):
    print(f"{n} - {m} = {n-m}")

def mul(n,m):
    print(f"{n} * {m} = {n*m}")

def div(n,m):
    print(f"{n} / {m} = {n/m}")

def rem(n,m):
    print(f"{n} % {m} = {n%m}")

print("CALCULATOR")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Remainder")
print("6.Quit")
run=True
while run:
    a=int(input("Enter your Option: "))
    if a==1:
        n = int(input("Enter First Value: "))
        m = int(input("Enter Second Value: "))
        add(n,m)
    elif a==2:
        n = int(input("Enter First Value: "))
        m = int(input("Enter Second Value: "))
        sub(n,m)
    elif a==3:
        n = int(input("Enter First Value: "))
        m = int(input("Enter Second Value: "))
        mul(n,m)
    elif a==4:
        n = int(input("Enter First Value: "))
        m = int(input("Enter Second Value: "))
        div(n,m)
    elif a==5:
        n = int(input("Enter First Value: "))
        m = int(input("Enter Second Value: "))
        rem(n,m)
    elif a==6:
        run=False
    else:
        print("INVALID OPTION")
