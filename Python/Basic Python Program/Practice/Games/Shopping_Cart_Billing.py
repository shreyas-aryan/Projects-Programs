#billing program
print("Shopping Cart PROG!!!")
foods=[]
prices=[]
n=True
i=0
while n:
    elem=input("Enter the Food You are Buying(q to quit): ")
    if elem=="q":
        break
    else:
        foods.append(elem)
        elem1 = float(input("Enter the Price of The Item: $"))
        prices.append(elem1)
        i += 1
print("-------YOUR CART-------")
for j in foods:
    print(j, end=" ")
total=0
for j in prices:
    total+=j
print()
print(f"TOTAL IS: {total}")
