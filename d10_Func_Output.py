import d10_art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Each function is paired with a symbol
operators: dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(d10_art.logo)
    result: float = 0
    first_num = float(input("What is your first number?: "))
    while True:

        for symbol in operators:
            print(symbol)
        operand = input("Operand, '*', '/', '+', or '-': ")

        second_num = float(input("What is your second number?: "))

        result: float = operators[operand](first_num, second_num)
        print(f"The result is: {result}")

        print(f"{first_num} {operand} {second_num} = {result}")

        another = input(f"Would you like to continue using the previous result of: {result}? 'y' for yes or 'n' for no: ")
        if another == "n":
            print("\n")
            # print("This program has ended...")
            # break
            calculator()
        elif another == "y":
            first_num = result
        elif another == "q" or "quit":
            print("\n")
            print("This program has quit")


calculator()


