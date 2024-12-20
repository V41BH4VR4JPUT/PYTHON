# for loop in python
#example 1

name = " vaibhav "
for i in name:
    print(i, end="-")
print("\n")
#example 2

CarBRands = ["BMW", "Audi", "Mercedes", "Toyota", "Ford"]
for x in CarBRands:
    print(x)
    for i in x:
        print(i, end="-")
    print("\n")    

#example 3
# for loop with range function

for v in range(0, 30 , 5):
    print(v , end="<")