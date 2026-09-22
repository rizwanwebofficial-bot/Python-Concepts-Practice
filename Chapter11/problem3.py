class Employee():
    salary=400
    increment=20
    
    
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment= ((salary/self.salary)-1)*100
    
    
e=Employee()
# print(e.salaryafterincrement)

salary=480
print(e.increment)