print ("***welcome in  tip-Calculator***")

bill = int(input("what is the total bill?\n $"))
friends = int(input("how many people seperate bill? \n")) 
bill_service =int(bill*12/100)

paid = int(bill)+int(bill_service)
each_one = paid // friends

print(f"servic is 12%  {bill_service}$")
print(round(bill_service + bill))
print(f"every one should be pay {each_one}$ ") 


