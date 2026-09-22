n = int(input("Enter a number: "))
def sum(n):
    if n == 0:
        return 0
    y = sum (n - 1)  + n 
    return y

print(sum(n))