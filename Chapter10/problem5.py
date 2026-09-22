

class Train:
    
    def __init__(self, ticketno, fare, fro, to):
        self.ticketno = ticketno
        self.fare = fare
        self.fro = fro
        self.to = to
        
    def book(self):
        print(f"The train has been booked and ticket no or seat number is {self.ticketno} and going from {self.fro} to {self.to}")
    
    def status(self):
        print(f"The booked seat number is {self.ticketno}")
    
    def fareinfo(self):
        print(f"The seat in the train has been booked for  {self.fare} Rs/--")
        
        
obj=Train(21, 5500, "Islamabad", "Sialkot")
obj.book()
obj.status()
obj.fareinfo()
    
    