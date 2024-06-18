import random as rd
import time

print("\t\t---------------------\n\t\tROCK PAPER SICSSOR\n\t\t---------------------\n")
print("Game rule:\n\t1)same to same result in dra\n\t2)Rock to Sicssor results in Rock win\n\t3)Scissor to Paper results in paper win\n\t4)Paper to Rock results in Paper win\n")
print("Condition:\n\t1)press 1 for rock\n\t2)Press 2 for scissor\n\t3)Press 3 for paper\n")
name=input("Enter your name:")
i=0
user_points=0
comp_points=0
while True:
    i=i+1
    comp=rd.randint(1,3)
    print(f"ROUND:{i}\n")
    user=int(input("enter the R,S,P as 1/2/3 and 4 to Exit:"))
    time.sleep(1)
    print(f"Comp as choose {comp}\n")
    print(f"User has choose {user}\n")
    if user==4:
        break
    if(comp==user):
        print("Both have choosen the same so its a \"DRAW\"\n ")
        time.sleep(1)
    elif(comp==1 and user==2 or comp==2 and user==3 or comp==3 and user==1):
        print("Computer has won this round!!!!\n")
        comp_points= comp_points +1
        print(f"Comp has scorde {comp_points} point !! Hurry up\n")
        time.sleep(1)
    elif(user==1 and comp==2 or user==2 and comp==3 or user==3 and comp==1):
        print(f"Congatulations  {name} you Won!!!!!")
        user_points=user_points+1
        print(f"{name} has scorde {user_points} points !! Hurry up\n")
        time.sleep(1)
   
    else:
        print(f"{name} You enterd wrong value!!!!\n")
        time.sleep(1)
time.sleep(2)
print(f"Total score comp:{comp_points}\nTotal score Lucky:{user_points}\n")
time.sleep(1)
print("Thanks for joining , Hope u had fun playing!!!")

    