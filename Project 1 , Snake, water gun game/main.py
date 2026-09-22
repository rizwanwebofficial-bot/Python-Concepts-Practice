'''
snake = 1
gun = 0
water = - 1

'''
import random

computer = random.choice([0, 1, -1])
user = input("Enter your choice (snake, gun, water): ")
userdict= {"snake":1, "gun":0, "water":-1}
reversedict= {1:"snake", 0:"gun", -1:"water"}

your=userdict[user]

print(f"The Computer selects:  {reversedict[computer]}\n The user selects: {reversedict[your]}")

if (your==1 and computer == 0):
    print("You Loose")
    
elif (your==1 and computer == 1):
    print("Draw")
    
elif (your==1 and computer == -1):
    print("You Win")
    
elif (your==-1 and computer == 0):
    print("You Win")
    
elif (your==-1 and computer == 1):
    print("You Loose")

elif (your==-1 and  computer == -1):
    print("Draw")
    
else:
    print("There is some error!!!")