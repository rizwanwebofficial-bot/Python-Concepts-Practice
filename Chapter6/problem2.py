marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))

# calculating percentage 
total_percentage = 100 * (marks1 + marks2 + marks3) / 300

if (total_percentage >= 40 and marks1>= 33 and marks2>= 33 and marks3>= 33):
    print("You are passed", "Your percentage is:", total_percentage)   
else:
    print("You are failed", "Your percentage is:", total_percentage)