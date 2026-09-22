class Calculator:
    def __init__(slf,n):
        slf.n=n
        
    def square(slf):
        print(f"the square of number is {slf.n*slf.n}")
    def cube(slf):
        print(f"the cube of number is {slf.n*slf.n*slf.n}")
        
    def squareroot(slf):
        print(f"the square of number is {slf.n**1/2}")
        
    @staticmethod
    def greeting():
        print("hello, how are you")
        
number=Calculator(4)
number.greeting()
number.square()
number.cube()
number.squareroot()