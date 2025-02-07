# Operator overloading in python

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __Str__(self):
        return "point= ({0},{1})".format(self.x,self.y)
    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1,2)
print(p1.x , p1.y)
p2 = Point(3,4)
print(p2.x , p2.y)

p3 = p1+ p2
print(p3.x , p3.y)