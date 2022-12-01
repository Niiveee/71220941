def add():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    add = a + b
    print(a , "+" , b, add)

def subtract():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    subtract = a - b
    print(a, "-" , b, multiply)

def multiply():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    multiply = a * b
    print(a, "*" , b, multiply)

def divide():
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
    divide = a / b
    print(a, "/", b, divide)

while  True:
    userInput = int(input("pilih rumus yang akan di pakai \n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n\n Enter Choice(1/2/3/4): "))
    if(userInput == 1):
        add()
    elif(userInput == 2):
        subtract()
    elif(userInput == 3):
        multiply()
    elif(userInput == 4):
        divide()
    else:
        break
    