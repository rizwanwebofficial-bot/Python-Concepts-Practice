# number = int(input("Enter a number: "))
# def multiplication_table(number):
#     for i in range(1, 11):
#         result = number * i
#         print(f"{number} x {i} = {result}")

# multiplication_table(number)

number = int(input("Enter a number: "))
def multiplication_table(number):
    for i in range(1, 11):
        result = number * (11-i)
        print(f"{number} x {11-i} = {result}")

multiplication_table(number)