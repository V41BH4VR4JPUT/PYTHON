# using match case statement
Day = input("Enter the day: ").strip().capitalize()
match Day :
    case "Monday":
        print("Today is Monday\n   You Should make a schedule for whole week and start working on it")
    case "Tuesday":
        print("Today is Tuesday\n  you should go to temple (bajrang bali day)")
    case "Wednesday":   
        print("Today is Wednesday\n  you should keep focus on your goals and work hard")
    case "Thursday":
        print("Today is Thursday\n   you almost there keep going")
    case "Friday":
        print("Today is Friday\n veryyyyy closeeee!!!!!!!!")
    case "Saturday":
        print("Today is Saturday\n you should finish your task so you can enjoy weekend")
    case "Sunday":  
        print("Today is Sunday\n you should rest and relax")
    case _:
        print("Invalid Day")