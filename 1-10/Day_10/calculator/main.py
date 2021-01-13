from art import logo

print(logo)


# Add
def add(num1, num2):
    return num1 + num2


# Substract
def substract(num1, num2):
    return num1 - num2


# Multiply
def multiply(num1, num2):
    return num1 * num2


# Divide
def divide(num1, num2):
    return num1 / num2

# Exponential
def exponential(num1, num2):
    return num1 ** num2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
    "**": exponential,
    }

def calculator():
    first = float(input("What's the first number?: "))

    for operation in operations:
        print(operation)

    continue_calculation = True

    while continue_calculation:
        option = input("Pick an operation: ")
        second = float(input("What's the next number?: "))
        calculation_function = operations[option]
        result = calculation_function(first, second)
        print(f"{first} {option} {second} = {result:.2f}")

        continue_option = input(f"Type 'y' to continue calculating with {result}, type 'r' to start a new  calculation, or type 'n' to exit: ").lower()

        if continue_option == 'y':
            first = result

        elif continue_option == 'r':
            continue_calculation = False
            calculator()
        elif continue_option == 'n':
            print("Goodbye!")
            continue_calculation = False
        else:
            print("Incorrect option, try again")


calculator()
