# Exception Handling
'''
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

Python try...except
try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

Syntax:
try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception

'''
# Example 1
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid  Input!")

print("Some imp lines of code")
print("End of program")
# Example 2
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]#list of two elements
    print(a[num])#Accessing the element of list using index
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")