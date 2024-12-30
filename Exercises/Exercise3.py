# Exercise -3 
"""
 KBC game
  * use lists for questions and answers
  * and also display the amount of money person won after each question
"""
def welcomeDisplay():
    str1 = "Welcome to KBC game"
    print(str1.center(80,'*'))
    print("Do you want to play the game?")
    i = input("Enter yes or no: ")
    if(i == "yes"):
        print("Great! Let's start the game")
        print("Choose option from A, B, C, D")
    else:
        print("Thank you for your time")
        exit()    

def KBC():
    Questions = ["Q1: Which of the following Python data types is immutable??",
                 "Q2: Which Brackets use in tuples?",
                 "Q3: Which Python keyword is used for function declarations?",
                 "Q4: Which of the following is the correct way to declare a Python dictionary?",
                 "Q5: Which of the following is the correct way to declare a Python list?"]
    OptionForQ1 = ["A. List","B. Tuple","C. Set","D. Dictionary"]
    OptionForQ2 = ["A. ()","B. []","C. {}","D. <>"]
    OptionForQ3 = ["A. def","B. function","C. func","D. define"]
    OptionForQ4 = ["A. {}","B. ()","C. []","D. <>"]
    OptionForQ5 = ["A. {}","B. ()","C. []","D. <>"]
    
    print(Questions[0])
    for i in OptionForQ1:
        print(i)
    ans1 = input("Enter your answer: ")
    if(ans1 == "B"):
        print("Congratulations! You have won 1000 rupees")
    else:
        print("Sorry! You have lost the game")
        exit()

    Amount = 1000
    print(f"Amount won: {Amount}")
    print(Questions[1])
    for i in OptionForQ2:
        print(i)
    ans2 = input("Enter your answer: ")
    if(ans2 == "A"):
        print("Congratulations! You have won 2000 rupees")
    else:
        print("Sorry! You have lost the game")
        exit()
    Amount = 2000 + Amount
    print(f"Amount won: {Amount}")

    print(Questions[2])
    for i in OptionForQ3:
        print(i)
    ans3 = input("Enter your answer: ")
    if(ans3 == "A"):
        print("Congratulations! You have won 3000 rupees")
    else:
        print("Sorry! You have lost the game")
        exit()
    Amount = 3000 + Amount
    print(f"Amount won: {Amount}")

    print(Questions[3])
    for i in OptionForQ4:
        print(i)
    ans4 = input("Enter your answer: ")
    if(ans4 == "A"):
        print("Congratulations! You have won 4000 rupees")
    else:
        print("Sorry! You have lost the game")
        exit()
    Amount = 4000 + Amount
    print(f"Amount won: {Amount}")

    print(Questions[4])
    for i in OptionForQ5:
        print(i)
    ans5 = input("Enter your answer: ")
    if(ans5 == "C"):
        print("Congratulations! You have won 5000 rupees")
    else:
        print("Sorry! You have lost the game")
        exit()
    Amount = 5000 + Amount
    print(f"Amount won: {Amount}")

    print("Congratulations! You have won the game")
    print(f"Total amount won: {Amount}")

def main():
    welcomeDisplay()
    KBC()
    a = input("Do you want to play again?\n")
    if(a == "yes"):
        KBC()
    elif(a == "no"):
        print("Thank you for your time")
        print("Hope you enjoyed the game")
        print("Have a nice day")
        F = input(" KYA KIJIYEGA IS DHAN RASHI KA ??\n")
        print(f" kya ucch vichar hai app is dhanrashi se {F} krenge!!!!")
        exit()

main()        
    