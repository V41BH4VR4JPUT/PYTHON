"""
Creating a Simple Project to understand the basics of Python Programming Language using the following concepts:
1. Print Statement
2. Escape Sequence Characters
3. Data Types and variables
4. Type-Casting
5. Strings 
6. String Slicing
7. String methods
8. taking user input

Creating a Greeting card Generator using above concepts

"""

# Greeting Card Generator
print("Welcome to the Greeting Card Generator!\n")
print("Let's create a personalized greeting for your loved ones. 🎉\n")

# Taking user input
name_of_the_recipient = input("Enter the name of the recipient: ")
name_of_the_sender = input("Enter the name of the sender: ")
occasion = input("Enter the occasion: ")
message = input("Enter the message: ")
# Type-Casting
name_of_the_recipient = str(name_of_the_recipient)
name_of_the_sender = str(name_of_the_sender)
occasion = str(occasion)
message = str(message)

# Printing the greeting card using string methods
print("\n" + "*" * 50)
print(occasion.center(50, " ").upper() + "\n")
print("Dear " + name_of_the_recipient.strip().title() + "\n")
print(message.capitalize() + "\n")
print("Warm Regards,")
print("From " + name_of_the_sender.strip().title())
print("*" * 50)
