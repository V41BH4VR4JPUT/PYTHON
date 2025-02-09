# Walrus operator (:=) in Python 3.8

Names = []
while(name := input("enter the names of your best friends:")) != "end":
    Names.append(name)
print(Names)