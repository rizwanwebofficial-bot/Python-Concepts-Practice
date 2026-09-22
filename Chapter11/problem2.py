class Animal():
    pass


class Pets(Animal):
    pass

class Dog(Pets):
    bark = "too loud"
    def barks(self):
        print(f"The dog was barking {self.bark}")
        
        
a=Dog()
a.barks()