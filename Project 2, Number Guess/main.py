import random
n = random.randint(1,50)
a=-1
guesses=0

while (a!=n):
    guesses +=1
    a= int(input("Enter a number"))
    # guesses +=1
    if(a>n):
        print("Enter lower number")
        
    else:
        print("Print higher number")
        
print(f"You have guessed the number {n} in the {guesses} attempt.")
        