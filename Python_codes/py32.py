# Raising Custom Errors

user = (input("ENTER THE NUMBER BETWEEN 5 AND 9  : "))
if (user == "quit"):
    print("You have entered quit")
elif int(user)<5 or int(user)>9:
    raise ValueError("You have entered wrong number")
else:
    print("You have entered correct number")        