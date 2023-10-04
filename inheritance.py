class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1
    
    def eat(self):
        print("Eat")
        
class Mammal(Animal):
    
    def __init__(self):
        print("Mammal Constructor")
        super().__init__()
        self.weight = 2
        
    def walk(self):
        print("Walk")
        
class Fish(Animal):
    
    def swim(self):
        print("Swim")                    
        
        
f = Mammal()
print(f.age)
print(f.weight)
f.walk()     