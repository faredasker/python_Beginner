import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',' J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
sympol = ['&','*','%','<','>','/','^','!','?', '@','$','+','=','|',]

nr_letters = int(input("how many letter you want\n"))
nr_numbers = int(input("how many numbers you want\n"))
nr_sympol = int(input("how many sympol you want\n"))

# Easy Level
# passoward = ""

# for char in range(1 , nr_letters +1):
#     passoward+=  random.choice(letters)
    
# for char in range(1 , nr_numbers +1):
#     passoward+= random.choice(numbers)    

# for char in range(1, nr_sympol +1):
#     passoward+= random.choice(sympol)

# print(passoward)   
    
    # Hard Level 
    
passoward_list= []

for char in range(1 , nr_letters +1):
    passoward_list+=  random.choice(letters)
    
for char in range(1 , nr_numbers +1):
    passoward_list+= random.choice(numbers)    

for char in range(1, nr_sympol +1):
    passoward_list+= random.choice(sympol)

print(passoward_list) 
random.shuffle(passoward_list)
print(passoward_list)

passoward = ""
for char in passoward_list:
    passoward+=char
print(f"your pass is {passoward}")    

  
    