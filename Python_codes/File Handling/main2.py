# Readlines() and writelines() methos in file handling

# file = open("File.txt", 'x')


# writelines() method is used to write a list of strings to a file
file = open("File.txt", 'w')
lines = ["1,2,3\n", "4,5,6\n", "7,8,9\n"]
file.writelines(lines)
file.close()

# readlines() method is used to read a file line by line
file = open("File.txt", 'r')

while True:
    line = file.readlines()
    if not line:
        break
    print(line)



