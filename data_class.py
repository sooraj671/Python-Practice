from collections import namedtuple

Point = namedtuple("Point", ["x","y"])
p1 = Point(x=2, y=3)
p2 = Point(x=2, y=3)
print(p1 == p2)