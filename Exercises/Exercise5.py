"""
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

Your program should ask whether you want to code or decode.

"""
import random

# Ask the user whether they want to code or decode
choice = input("Do you want to code or decode? ").strip().lower()

word = str(input("Enter the word: "))

if choice == "code":
    # for coding the new language
    if len(word) >= 3:
        word = word[1:] + word[0]
        word = random.choice("qwertyuiopasdfghjklzxcvbnm") + random.choice("qwertyuiopasdfghjklzxcvbnm") + random.choice("qwertyuiopasdfghjklzxcvbnm") + (word + random.choice("qwertyuiopasdfghjklzxcvbnm")) + random.choice("qwertyuiopasdfghjklzxcvbnm") + random.choice("qwertyuiopasdfghjklzxcvbnm")
    else:
        word = word[::-1]
    print("Encoded word:", word)

elif choice == "decode":
    # for decoding the new language
    if len(word) >= 9:  # Since we added 6 random characters during encoding
        word = word[3:-3]  # Remove the first 3 and last 3 characters
        word = word[-1] + word[:-1]  # Move the last character to the beginning
    else:
        word = word[::-1]  # Reverse the string if it's less than 3 characters
    print("Decoded word:", word)

else:
    print("Invalid choice")