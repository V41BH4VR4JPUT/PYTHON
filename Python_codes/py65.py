# Regular Expression in python

import re

pattern = r"Hello"
text = "Hello world"

match = re.match(pattern, text)
if match:
    print("Match Found:" , match.group())
else:
    print("No match")
pattern = r"World"
text = "Hello, World!"

match = re.search(pattern, text)
if match:
    print("Match found at position:", match.start()) 

pattern = r"\d+"  # Match one or more digits
text = "My phone number is 12345 and my pin is 6789."

matches = re.findall(pattern, text)
print("Found numbers:", matches)

text = "I like cats. Cats are cute."
pattern = r"cats"  # Case-sensitive
replacement = "dogs"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)

text = "apple, banana; orange:grape"
pattern = r"[,;:]"

result = re.split(pattern, text)
print(result)

pattern = r"(\d{3})-(\d{3})-(\d{4})"  # Phone number format (XXX-XXX-XXXX)
text = "My contact is 123-456-7890."

match = re.search(pattern, text)
if match:
    print("Area code:", match.group(1))   # Output: 123
    print("Prefix:", match.group(2))      # Output: 456
    print("Line number:", match.group(3))

pattern = re.compile(r"\bPython\b", re.IGNORECASE)

text1 = "I love Python programming."
text2 = "python is great."

print(bool(pattern.search(text1)))  # Output: True
print(bool(pattern.search(text2)))
