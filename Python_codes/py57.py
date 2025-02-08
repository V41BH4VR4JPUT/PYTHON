# Hybrid Inheritance in python

class parent1 :
    def __init__(self , name , id):
        self.name = name
        self.id = id
    def display(self):
        print(f"Name: {self.name} and ID: {self.id}")

class parent2 :
    def __init__(self , age):
        self.age = age
    def display(self):
        print(f"Age: {self.age}")

class child(parent1 , parent2):
    def __init__(self , name , id , age):
        parent1.__init__(self , name , id)
        parent2.__init__(self , age)
    def display(self):
        parent1.display(self)
        parent2.display(self)

class grandchild(child):
    def __init__(self , name , id , age , height):
        child.__init__(self , name , id , age)
        self.height = height
    def display(self):
        child.display(self)
        print(f"Height: {self.height}")

g = grandchild("John" , 101 , 25 , 5.8)
g.display()