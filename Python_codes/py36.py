"""
Global variable and local variable
"""

x = 5
print (f"the value of x is {x} bacause it is an global variable and it can't be changed in function.")

def func():
    global x 
    x = 25
    print (f"the value of x is {x} because it is an global variable and we changed it with global keyword.")
    x = 10
    print (f"the value of x is {x} because it is an local variable.")

print (f"the value of x is {x} bacause it is an global variable.")
func()
print (f"the value of x is {x} bacause its value changed after fucntion call.")