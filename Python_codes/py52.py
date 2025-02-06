# Overriding in python

class shape:
    def area(self):
        print("Calculating Area.....")

class square(shape):
    def __init__(self ,side):
        self.side = side
    def area(self):
        print("Calculating Area of Square  ")
        super().area()
        return self.side * self.side

s = square(5)   
print(s.area())

