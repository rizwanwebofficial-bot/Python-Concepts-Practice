a = int(input("Enter an number: "))
b = int(input("Enter an number: "))
c = int(input("Enter an number: "))

def largest_number(a, b, c):

    if a > b and a > c:
        print(f"{a} is the largest number.")
    elif b > a and b > c:
        print(f"{b} is the largest number.")
    else:
        print(f"{c} is the largest number.")
        

largest_number(a,b,c)