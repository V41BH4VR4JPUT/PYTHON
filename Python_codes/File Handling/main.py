# open() for opening file
# x for creating file
f = open("Textfile.txt", "x")

# w for writing in file
f = open("Textfile.txt", "w")
f.write("Hey Buddy!!!\n")
f.close()

# a for appending file
f = open("Textfile.txt", "a")
f.write("How was your holidays?\n")

# r for reading file
f = open("Textfile.txt", "r")
text = f.read()
print(text)

# rt for reading text file
f = open("Textfile.txt", "rt")
text = f.read()
print(text)
   
# rb for reading binary file
f = open("Textfile.txt", "rb")
text = f.read()
print(text)

# close() for closing file
f.close()