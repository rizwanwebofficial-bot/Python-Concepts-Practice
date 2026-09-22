numbers=[]

number1= int(input("Enter the first number: "))
numbers.append(number1)
number2= int(input("Enter the second number: "))
numbers.append(number2)
number3= int(input("Enter the third number: "))
numbers.append(number3)
number4= int(input("Enter the fourth number: "))
numbers.append(number4)

largest_number = max(numbers)
print("The largest number is:", largest_number)
