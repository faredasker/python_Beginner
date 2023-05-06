import random 
from hangman_art import stages
from hangman_words import word_list
 
end_of_game = False 
word_choise = random.choice(word_list)
word_length = len(word_choise)

lives = 6
print(f'the solution is {word_choise}')          

display = []
for _ in range(word_length):
    display += "_"
 
while not end_of_game:    
    guess = input('guess letter/   ').lower()
    
    if guess in display:
        print(f"you.ve already guessed {guess}")
 
    for position in range(word_length):
        letter = word_choise[position] 
        # print(f"current position:{position}\n cuurent letter:{letter}\n gussed letter:{letter}")
        if letter == guess:
            display[position] = letter
    
    if guess not in word_choise:
        lives -=1
        if lives == 0:
            end_of_game = True 
            print("you lose")    
     
    print(f"{' '.join(display)}")  

    if "_" not in display:
        end_of_game = True   
        print("you win")

    print(stages[lives])
    