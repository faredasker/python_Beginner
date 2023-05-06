print("Welcome in pizza resturant")

type_pizza = input("what type of pizza you want [4cheese - chicken - margreta]   ")
pizza = input("which size you want [S - M - L]   ")
peprony = input("do you want add peprony [Yes \ No]  ")
cheese = input("do you want add extra cheese [Yes \ No]  ")

bill = 0

if type_pizza == "4cheese":
    if pizza == "S":
        bill+=80
    elif pizza == "M":
        bill+=95
    elif pizza == "L":
        bill+=110    
        
if type_pizza == "chicken":
    if pizza == "S":
        bill+=95
    elif pizza == "M":
        bill+=115
    elif pizza == "L":
        bill+=125

if type_pizza == "margreta":
    if pizza =="S":
        bill+=70 
    elif pizza == "M":
        bill+=85
    elif pizza == "L":
        bill+=105                       
               
if peprony == "Yes":
    if pizza == "S":
      bill+=15
    elif pizza == "M":
        bill+=20
    elif pizza == "L":
        bill+=25    
elif peprony == "No":
    bill+=0


if cheese == "Yes":
    bill+=10
elif cheese == "No":
    bill+=0            
    
print(f"total bill is {bill} pound")    
