# class Employee:
#     name = "John Doe"
#     age = 30
#     salary = 50000
    
# print(Employee.name)

class Employee:
    name = "John Doe"
    age = 30
    salary = 50000
    
    def greet(self):
        print (f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    def display_salary(self):
        print (f"My salary is {self.salary}.")
    
    
harry = Employee()
harry.display_salary()

harry.greet()