# Exercise2  
""" Time module in python is built in module 
    strftime() function is used to print the time in string format.
    && = and
    || = or
    below exercise done by using if-elif-else statements 
"""
import time
timestamp = time.strftime('%H : %M : %S')
print(timestamp)

hour = int(time.strftime('%H'))

if(hour> 12 and hour< 17):
    print(" Good After Noon \n")

elif(hour< 12 ):
    print(" Good Morning \n")

elif( hour>= 17):
    print("Good Evening \n")  

else :
    print(" Invalid Time \n")

print(" Have a nice day!!")