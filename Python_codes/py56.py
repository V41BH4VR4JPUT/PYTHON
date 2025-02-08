# MultiLevel inheritance in Python

class grandfather:
    def __init__(self , Biradari , height):
        self.Biradari = Biradari
        self.height = height
    def display(self):
        print(f"Biradari: {self.Biradari} \n  Height: {self.height}") 

class father(grandfather):
    def __init__(self , Biradari , height , jaydaat):
        grandfather.__init__(self , Biradari , height)
        self.jaydaat = jaydaat
    def display(self):
        grandfather.display(self)
        print(f"  jaydaat: {self.jaydaat}")

class child(father):
    def __init__(self , Biradari , height , jaydaat , Lugai):
        father.__init__(self , Biradari , height , jaydaat)
        self.Lugai = Lugai
    def display(self):
        father.display(self)
        print(f"  Lugai: {self.Lugai}")

v = child("rajput" , 5.8 , "2.5 crore" , "ToTo")
v.display()