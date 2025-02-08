# Single Inheritance in Python
class parent1:
    def __init__(self, name , id):
        self.name = name
        self.id = id
    def diaplay(self):
        print(f"Name: {self.name} and ID: {self.id}")
    
class child(parent1):
    def __init__(self , name , id , age):
        parent1.__init__(self , name , id)
        self.age = age
    def diaplay(self):
        parent1.diaplay(self)
        print(f"Age: {self.age}")

c = child("John" , 101 , 25)
c.diaplay()