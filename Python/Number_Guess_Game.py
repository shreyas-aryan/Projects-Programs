#number guessing game
from random import randint
print("Random Number Guessing Game!!")
n=randint(0,101)
temphigh=n+5
templow=n-5
a=int(input("Enter the number of guesses: "))
i=1
while i<=a+1:
    b=int(input(f"Enter your {i}th Guess: "))
    if b==n:
        print(f"You Guessed it correct it was {b}")
        break
    elif b>temphigh:
        print("Guessing TOO HIGH")
    elif b<temphigh and b>n:
        print("You are a bit High")
    elif b > templow and b < n:
        print("You are a bit Low")
    else:
        print("Guessing TOO LOW")
    i+=1
print(f"The answer was: {n}")
