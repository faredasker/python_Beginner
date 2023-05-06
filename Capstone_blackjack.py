import random
from art_blackjack import logo


def deal_card():
    """ Returns random cards from the dec"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """ take alist of cards and return a score"""
    if sum(cards) == 21 and len(cards) ==2:
            return 0 
     
    if 11 in cards and sum(cards)>21:
         cards.remove(11)
         cards.append(1)
    return sum(cards)

def compare(user_score , computer_score):
    """ if you and computer both you are lose """
    if user_score > 21 and computer_score >21:
        return "you went over you lose"  
    
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose has ablackjack"
    elif user_score == 0 :
        return "win with blackjack"
    elif user_score>21:
        return "you lose over 21"
    elif computer_score >21:
        return "you win "
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"
    
def play_game():
    print(logo) 
                
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card()) 
        computer_card.append(deal_card())
    
    while not is_game_over:
        
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)    
        print(f"your cards: {user_card}, cuurent score: {user_score}")
        print(f"computer first card : {computer_card[0]}")
        
        if user_score == 0 or computer_score==0 or user_score>21:
            is_game_over = True 
        else:
            user_should_deal = input("type 'y' to get another card type'n' to pass")        
            if user_should_deal =="y":
                user_card.append(deal_card())
            else:
                is_game_over=True
    
    while computer_score != 0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)  
        
    print (f"your final: {user_card}, final score: {user_score}")              
    print (f"computer final: {computer_card}, final score: {computer_score}")              
    print (compare(user_score , computer_score))
    
play_game()                
    
        

 





