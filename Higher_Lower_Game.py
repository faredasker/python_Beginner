from data_higher_lower import data
import random
from art_higher_lower import logo ,vs


# def get_random_account():
#     """ get random data"""
#     return random.choice(data)


def format_data(account):
    """ format account into printable format: name ,description,country"""
    name = account["name"]
    description = account["description"]
    country = account ["country"]
    return f"{name} a {description} , from {country}"


def check_answer(guess , a_followers ,b_followers):
    """take the user guess and follower counts and returns if got it right """
    if a_followers > b_followers:
        return guess == "a"  
    else:
        return guess == "b"
    
    
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    guess = input("guess who has more follower? 'a' or 'b':  " ).lower()


    a_follower_count = account_a["follower_count"] 
    b_follower_count = account_b["follower_count"]    
    is_correct = check_answer(guess , a_follower_count, b_follower_count)     
        
    if is_correct:
        score +=1
        print(f" right your score is {score}")
    else:
        game_should_continue = False
        print(f"sorry it's wrong your score is {score}")    
