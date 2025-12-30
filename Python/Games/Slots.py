# Slot Machine, Gambling
import random
def emojis(s):
    if s == 0:
        return "🪝"
    elif s == 1:
        return "💣"
    elif s == 2:
        return "💸"
    elif s == 3:
        return "⚖️"
    elif s == 4:
        return "🩻"
    elif s == 5:
        return "🏺"

print("---------SLOTS---------")
print("START BALANCE = $10,000")
m = 10000
while True:
    print(f"YOUR BALANCE: ${m}")
    p = input("Do you wanna play?(y/n): ")
    if p.lower() != "y" or m <= 100:
        print("Exiting slots...")
        break
    s1 = random.randint(0, 5)
    s2 = random.randint(0, 5)
    s3 = random.randint(0, 5)
    print("--------------------")
    print(f"| {emojis(s1)} | {emojis(s2)} | {emojis(s3)} |")
    print("--------------------")
    if s1 == s2 == s3:
        if s1 == 0:
            print("YOU WIN GOLDEN HOOK + $15000")
            n = 15000
        elif s1 == 2:
            print("YOU WON, MAX WIN + $20000")
            n = 20000
        elif s1 == 1:
            print("YOU LOST, BIG LOSS - $5000")
            n = -5000
        else:
            print("YOU WON JACKPOT!!!!!! + $10000")
            n = 10000
    elif s1 == s2 or s2 == s3 or s1 == s3:
        if (s1 == s2 == 1) or (s2 == s3 == 1) or (s1 == s3 == 1):
            print("YOU LOST - $2500")
            n = -2500
        else:
            print("YOU WIN!!! + $2000")
            n = 2000
    else:
        print("YOU LOSE :( - $1000")
        n = -1000
    m += n
