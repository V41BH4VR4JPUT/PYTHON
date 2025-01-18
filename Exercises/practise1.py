# Just a practise set till date
a = 5
b = 9
print("The values of a is", a, "and b is", b)
st = """We define the values of a and b as shown above. Now we will 
perform some operation on these values.\n"""
print(st) 
st1 = ''' operations we perform are:\n
1. addition\n2. subtraction\n3. multiplication\n4. division\n5. floor division\n6. modulus\n7. exponential\n'''
print(st1)
print("Addition of a and b is", a + b)
print("Subtraction of a and b is", a - b)
print("Multiplication of a and b is", a * b)
print("Division of a and b is", a / b)
print("Floor division of a and b is", a // b)
print("Modulus of a and b is", a % b)
print("Exponential of a and b is", a ** b,"\n")  

st2 = ''' Now we see the type of every value we obtained\n'''
print(st2)
print("type of value obtained of a", type(a))
print("type of value obtained of b", type(b))
print("type of value obtained of a + b", type(a + b))
print("type of value obtained of a - b", type(a - b))
print("type of value obtained of a * b", type(a * b))
print("type of value obtained of a / b", type(a / b))
print("type of value obtained of a // b", type(a // b))
print("type of value obtained of a % b", type(a % b))
print("type of value obtained of a**b", type(a ** b),"\n")

"""
if class contains two constructors then it will execute the last one
"""
class cons:
    def __init__(self):
        print("I am a constructor")

    def __init__(self):
        print("Hello , I am a constructor")

Obj = cons()