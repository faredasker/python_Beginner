def add(n1, n2):
    return n1+n2
    
def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2
                
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}    
def calculator(): 
    num1 =float(input("enter first number\n"))
    for sympol in operations:
        print(sympol)

    again = True
    while again:
        num2 = float(input("enter second number\n"))
        sympol = input("pick an operation\n")
        calculation = operations[sympol]
        answer = calculation(num1,num2)

        print(f"{num1} {sympol} {num2} = {answer}")
        
        if input(f"type 'y' to continue with {answer} or 'n' to start new \n") =='y':
            num1 = answer
        else:
            again = False
            calculator()
calculator()   