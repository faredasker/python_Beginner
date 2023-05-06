print("Welcome to Treasure Island.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input("do you swim or wait boat \  ")
    if choice2 == "wait":
        choice3 = input("choose your color 'red'or'blue'or'yellow'/   ")
        if choice3=="red":
            print("you are fire")
        elif choice3=="blue":
            print("you attacked from monester")    
        elif choice3 == "yellow":
            print("you are winner")
    else:
        print("game over you ar die early")        
else:
    print("game over")           