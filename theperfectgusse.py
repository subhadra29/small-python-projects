import random
gusses=[]
computernum= random.randint(1,100)

yournum=int(input("chosse a number between 1 to 100"))

while(yournum != computernum):
    if(yournum>computernum):
        gusses.append(yournum)
        with open("gusses.txt", "w") as g:
            for i in gusses:
                g.write(str(i) + "\n")
        print("gusse a low number")
        yournum=int(input("try another number"))

    elif(yournum<computernum):
        gusses.append(yournum)
        with open("gusses.txt", "w") as g:
            for i in gusses:
                g.write(str(i) + "\n")
        print("gusse a high number")
        yournum=int(input("try another number"))

if(yournum== computernum):
    gusses.append(yournum)
    with open("gusses.txt", "w") as g:
        for i in gusses:
            g.write(str(i) + "\n")
    print(f"you took {len(gusses)} gusses")
    print("you gussed it right!!")
