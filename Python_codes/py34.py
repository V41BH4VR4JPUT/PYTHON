#Enumerate Function in Python

marks = [90, 25 , 67 , 45 , 80]
for index , mark in enumerate(marks):
    print(f'{index+1}: {mark}')
    if mark < 50:
        print('failed')
    else:
        print('passed')
print("\n")
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)
print("\n")
# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
