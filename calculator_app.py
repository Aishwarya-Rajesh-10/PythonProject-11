import os
import platform

logo = r"""
 _____________________
| _________________ |
| | Pythonista 0. | |
| |_________________| |
| ___ ___ ___ ___ |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

   C A L C U L A T O R
"""

def clear_screen():

    if platform.system().lower().startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def add(n1, n2): return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        return "Error (divide by zero)"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:

        print("\nPick an operation:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Enter your operation: ")
        num2 = float(input("What's the next number?: "))

        calc_function = operations.get(operation_symbol)
        if not calc_function:
            print("Invalid operation. Try again.")
            continue

        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        next_step = input(
            f"Type 'y' to continue calculating with {answer}, "
            "or type 'n' to start a new calculation: "
        ).lower()

        if next_step == "y":
            num1 = answer
        else:
            clear_screen()
            calculator()
if __name__ == "__main__":
    calculator()