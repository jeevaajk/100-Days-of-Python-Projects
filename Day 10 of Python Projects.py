print(''' _____________________
|  _________________  |
| | JK           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    print("Welcome to JK's Calculator...!")
    num1 = float(input("Enter First Number: "))
    should_continue = True
    while should_continue:
        print("Select operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == "1":
            num2 = float(input("Enter Second Number: "))
            answer = add(num1, num2)
            print(f"{num1} + {num2} = {answer}")
            num1 = answer
        elif choice == "2":
            num2 = float(input("Enter Second Number: "))
            answer = subtract(num1, num2)
            print(f"{num1} - {num2} = {answer}")
            num1 = answer
        elif choice == "3":
            num2 = float(input("Enter Second Number: "))
            answer = multiply(num1, num2)
            print(f"{num1} * {num2} = {answer}")
            num1 = answer
        elif choice == "4":
            num2 = float(input("Enter Second Number: "))
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                answer = divide(num1, num2)
                print(f"{num1} / {num2} = {answer}")
                num1 = answer
        elif choice == "5":
            should_continue = False
            print("Exiting the calculator. Goodbye!")
        else:
            print("Invalid input. Please select a valid option.")

calculator()
