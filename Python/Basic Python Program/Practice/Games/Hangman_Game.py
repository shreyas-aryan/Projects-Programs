#HANGMAN GAME
import random
def dia(c):
    if c==1:
        print('''
                 0''')
    elif c==2:
        print('''
                 0
                 |''')
    elif c==3:
        print('''
                 0
                 |\\''')
    elif c==4:
        print('''
                 0
                /|\\''')
    elif c==5:
        print('''
                 0
                /|\\
                 |''')
    elif c==6:
        print('''
                 0
                /|\\
                 |
                  \\''')
    else:
        print('''
                 0
                /|\\
                 |
                / \\''')

l1=["apple", "mango", "orange", "seeds"]
index=random.randint(0,(len(l1)-1))
word=l1[index]
print("___________________________")
print("!!!!WELCOME TO HANGMAN!!!!")
print("___________________________")
print("----HANGMAN HAS 7 LIMBS----")
print(f"THIS IS A {len(word)} LETTER WORD")
for i in word:
    print("'_' ",end="")
p=[]
for i in range(0,len(word)):
    p.append("_")
print()
c=0
for i in range(0,(len(word)+7)):
    print()
    g=input("Enter Your Guess (single character): ")
    guess=g.lower()
    if len(guess)!=1:
        print("ERROR: ENTERED MORE THAN 1 OR NONE CHARACTER, HANGMAN GAME!")
        break
    a=[]
    for i in range(0,len(word)):
        if guess==word[i]:
            a.append(i)
    if a:
        print("CORRECT GUESS!")
        for j in a:
            p[j]=word[j]
        for i in p:
            print(i,end=" ")
        print()
    else:
        c+=1
        print("INCORRECT GUESS")
        dia(c)
        print("HANGMAN GREW!")
    z=0
    for i in range(0,len(word)):
        if word[i]==p[i]:
            z+=1
    if z==len(word):
        print("U WIN, GUESSED ENTIRELY CORRECT!!!")
        break
    if c==7:
        print("U LOST, TRY AGAIN!!")
        break
