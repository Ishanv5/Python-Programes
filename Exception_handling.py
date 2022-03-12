while True:
    try:
        age=int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid Input....... Retype it .........")
    except:
        print("Unexcepted input error.......")
    
if age<18:
    print("You can't Play this game")
else:
    print("You can play this game")