class twodvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        
    def show(self):
        print(f"The twodvectors are {self.i}i+{self.j}j") 
        
               
class threedvector(twodvector):
    
    def __init__(self,k,i,j):
        super().__init__(i,j)
        self.k=k
        
    def show(self):
        print(f"The threedvectors are {self.i}i+{self.j}j+{self.k}k")
        
a=twodvector(2,4)
b=threedvector(2,4,5)

a.show()
b.show()

        