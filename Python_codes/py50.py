"""
dic() 
__dict__
help()

function usage:
"""

class A:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def __str__(self):
        return f"{self.a} {self.b} {self.c}"

e1 = A()
print(e1.__dict__)

print(dir(e1))

help(e1)