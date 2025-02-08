# Hiearchial Inheritance in Python

class parent:
    def func1(self):
        print("This is function 1")

class child1(parent):
    def func2(self):
        print("This is function 2")

class child2(parent):
    def func3(self):
        print("This is function 3")

object1 = child1()
object2 = child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
