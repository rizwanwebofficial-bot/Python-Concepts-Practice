class Vector():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    
    
    def __len__(self):
        return 3
    
    
v1=Vector(1,2,3)
print (len(v1))