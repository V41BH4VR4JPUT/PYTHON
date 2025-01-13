# using seek() , tell() and truncate() function in file handling

# file =  open("Text.txt" , 'x') 

file = open("Text.txt" , 'w')
file.write("Hello world")
file.seek(0)
print(file.tell())
file.truncate(5)
print(file.tell())

