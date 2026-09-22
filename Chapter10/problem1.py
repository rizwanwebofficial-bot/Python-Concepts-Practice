

class Programmer:
    def __init__(self, name, age, salary):
        self.name = name
        self.age= age
        self.salary= salary
        
details = Programmer("Rizwan", 18, 120000)
print(details.name, details.age, details.salary)

detail = Programmer("Ali",19,130000)
print(detail.name, detail.salary, detail.age)
