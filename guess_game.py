print("welcom to guues number game")
logo = """ |  __ \                         | |  | |                                    | |                
| |  \/ _   _   ___   ___  ___  | |_ | |__    ___   _ __   _   _  _ __ ___  | |__    ___  _ __ 
| | __ | | | | / _ \ / _ \/ __| | __|| '_ \  / _ \ | '_ \ | | | || '_ ` _ \ | '_ \  / _ \| '__|
| |_\ \| |_| ||  __/|  __/\__ \ | |_ | | | ||  __/ | | | || |_| || | | | | || |_) ||  __/| |   
 \____/ \__,_| \___| \___||___/  \__||_| |_| \___| |_| |_| \__,_||_| |_| |_||_.__/  \___||_| 
"""

print (logo)
from random import randint

easy_level = 10
hard_level = 5


def check_answer(user_guess , answer,turns):
    """ check answer against user guess . return number of turns """
    if user_guess > answer:
        print(" too high")
        return turns -1
    elif user_guess < answer:
        print(" too low") 
        return turns -1
    else:
        print(f"this is answer {answer}.")
        
        
def difficult():
    level = input("type 'h' for hard or 'e' for easy\n")
    if level == "h":
        return hard_level
    elif level == "e":
        return easy_level   
    
     
def game():
    answer  = randint(1,100) 
    print(f"the correct answer is {answer}")

    turns = difficult()

    user_guess = 0  
    while user_guess != answer: 
        print(f"you have {turns} attempts to guess")
 
        user_guess = int(input("make a guess\n"))  
        turns = check_answer(user_guess, answer , turns)
        if turns == 0:
            print ("you've run out of guesses, you lose")
            return
        elif user_guess != answer:
            print("guess again ")
    
game()