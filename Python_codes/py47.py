# Static method in python

class Ex:
    @staticmethod
    def add():
        print("This is a static method")

    def Sub(self , a , b):
        return a - b

e = Ex()
print(e.add())
print(e.Sub(10, 5))