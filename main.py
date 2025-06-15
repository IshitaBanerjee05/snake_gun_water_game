import random
computer=random.choice([1,0,-1])
youstr=input("enter your choice: ")
youDict={"s": 1, "w":-1, "g":0}
reverseDict={1:"Snake", -1:"Water" , 0:"Gun"}
you=youDict[youstr]
print(f"your chooce {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("it's a draw")
else:
    if(computer==-1 and you==1):
        print("you win!")

    elif(computer==-1 and you==0):
        print("you lose!")

    elif(computer==1 and you==-1):
        print("you lose!")

    elif(computer==1 and you==0):
        print("you win!")

    elif(computer==0 and you==1):
        print("you win!")

    elif(computer==0 and you==-1):
        print("you win!")

    else:
        print("something went wrong")