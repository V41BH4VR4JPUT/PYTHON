# Constructors in python

class person :
    #  def __init__(self): # Default Constructor
    #       self.name = "vaibhav"
    #       self.age = 22
    #       self.occupation = "student"
     def __init__(self , name , age , occupation): # Parameterized Constructor
          self.name = name
          self.age = age
          self.occupation = occupation

     def info(self):
          print(f"Name : {self.name} \nAge : {self.age} \nOccupation : {self.occupation}")

# a = person() # Default Constructor calling
# a.info()
b = person("Totoo" , 23 , "student") # Parameterized Constructor calling
b.info()