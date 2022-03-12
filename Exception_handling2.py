while True:     
     try:
          nos=int(input("Enter a number:  "))
          break
     except ValueError:
         print("You did not entered Integer........ Retype it....")
     except:
         print("Unexcepted error")
     else:
        print(f"user_input={nos}")
        break
     finally:
        print("Finally block....")
    