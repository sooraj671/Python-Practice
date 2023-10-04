class Point:
    defualt_color = "red"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point ({self.x} , {self.y})")
    
    @classmethod
    def zero(cls):
        return cls(0,0)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
point = Point(2,2)
print(point.defualt_color)
point.draw()
print(Point.defualt_color)

point1 = Point.zero()
point1.draw()           
           
print(point1.__str__())
print(str(point))
     
print(point == point1)
print(point > point1)
print(point+point1)