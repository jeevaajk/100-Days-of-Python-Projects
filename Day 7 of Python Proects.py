# Simple Calculator in Python
print('''    ____    _    _     ____ _   _ _        _  _____ ___  ____  
  / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \ 
 | |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) |
 | |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ < 
  \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_\
                                                              ''')
def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero not allowed!")
    else:
        print("Invalid operator!")

calculator()

