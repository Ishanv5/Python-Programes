winning_nos=27
user_input=input("Guess nos between 1 to 100....")
user_input=int(user_input)
if user_input == winning_nos:
    print("You won......")
else:
    if user_input < winning_nos:
        print("Too low...")
    else:
        print("Too high...")