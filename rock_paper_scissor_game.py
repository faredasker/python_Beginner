import random   

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

 
game_image = [rock , paper , scissors]
user = int(input("enter your choose \ 0 rock or 1 paper or 2 scissor?   "))
computer = random.randint(0,1)

print (game_image[computer])
if user >= 3 or user <= 0:
    print("you typed an invalid number, you lose!")
    
elif  user == 0 and computer ==2:
    print("You win!")   
elif computer == 0 and user ==2:
    print("you lose")
elif computer > user:
    print("you lose")
elif user > computer:
    print("you win")  
elif computer == user :
    print("It's a draw")          
