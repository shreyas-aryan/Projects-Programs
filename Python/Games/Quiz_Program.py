#quiz with answer checking
ques=("Which keyword is used to define a function in Python?",
      "Which of the following is an even number?",
      "What is the capital of India?",
      "Which symbol is used for comments in Python?")
options=(("a) func","b) define","c) def","d) function"),
         ("a) 3","b) 5","c) 8","d) 9"),
         ("a) Mumbai","b) Delhi","c) Kolkata","d) Chennai"),
         ("a) //","b) /* */","c) #","d) --"))
ans=("c","c","b","c")
guess=[]
chk=0
for i in range(0,4,1):
    print(ques[i])
    for j in options[i]:
        print(j)
    elem=input("Enter your guess: ")
    guess.append(elem)
for i in range(0,4,1):
    if ans[i]==guess[i]:
        chk+=1
print("Answers: ",end=" ")
for i in ans:
    print(i,end=" ")
print()
print("Guesses: ",end=" ")
for i in guess:
    print(i,end=" ")
print()
print(f"Total Score is: {(chk/4)*100}")
