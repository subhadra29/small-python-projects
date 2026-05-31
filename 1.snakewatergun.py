import random

num = random.choice([1, 0, -1])

computerchoice=num
inputt= input("Enter your choice (snake,water,gun) : ")
value ={
    "snake": 1,
    "water":0,
    "gun":-1

}
yourchoice=value[inputt]
key = [k for k, v in value.items() if v == computerchoice]


if(yourchoice==computerchoice):
    print("draw!!!!!!!(try again i think you will win ;)")
else:
    if(yourchoice==1 and computerchoice==0):
        print("you win ;) ")
    elif(yourchoice==0 and computerchoice==-1):
        print("you win ;) ")
    elif(yourchoice==-1 and computerchoice==1):
        print("you win ;) ")
    elif(yourchoice==1 and computerchoice==-1):
        print("you loose :( ")
    elif(yourchoice==0 and computerchoice==1):
        print("you loose :( ")
    elif(yourchoice==-1 and computerchoice==0):
        print("you loose :( ")
print(f"Your choice : ['{inputt}']", f"computer,s choice: {key}")
print("thank you for playing my game!")
    


