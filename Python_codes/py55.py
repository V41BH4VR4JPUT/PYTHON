# Multiple Inheritance in Python

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
    
c = child("John" , 101 , 25)
c.display()