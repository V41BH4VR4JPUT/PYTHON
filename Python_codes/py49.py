"""
Class methods

"""

class person:
    def __init__(self , name , age , occupation): # Parameterized Constructor
         self.name = name
         self.age = age
         self.occupation = occupation

    def display(self):
         print(f"{self.name} is {self.age} years old and is a {self.occupation}")

    @classmethod
    def from_string(cls , string):
        name , age , occupation = string.split(",")
        return cls(name , age , occupation)
    
e1 = person("John" , 25 , "Software Engineer")
e1.display()
e1.from_string("Mike,30,Doctor").display()
