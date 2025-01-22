# getters and setters in python

class p:
    def __init__(self , value):
        self._value = value

    @property 
    def value(self):
        print("getter method called")
        return self._value
    
    @value.setter
    def value(self , new_value):
        print("setter method called")
        self._value = new_value

obj = p(10)
print(obj.value)
obj.value = 20
print(obj.value)