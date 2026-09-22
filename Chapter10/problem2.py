class Calculator:
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f"the square of number is {self.n*self.n}")
    def cube(self):
        print(f"the cube of number is {self.n*self.n*self.n}")
        
    def squareroot(self):
        print(f"the square of number is {self.n**1/2}")
        
number=Calculator(4)
number.square()
number.cube()
number.squareroot()