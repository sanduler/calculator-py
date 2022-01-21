from background import logo

print(logo)


def add(n1, n2):
    """This function takes integers and returns a sum"""
    return n1 + n2


def subtract(n1, n2):
    """This functions takes integers and returns a difference"""
    return n1 - n2


def multiply(n1, n2):
    """This function takes integers and returns a product"""
    return n1 * n2


def divide(n1, n2):
    """This function takes integers and returns a quotient"""
    if n2 == 0:
        return("Undefined")
    else:
        return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    """This stores the last calculated value and continues to calculation. Else, the function uses recursion to start a fresh calculation."""
    num1 = int(input("what is the first number?: "))
    for symbl in operations:
        print(symbl)
    should_continue = True
    while should_continue:
        num2 = int(input("what is the next number?: "))
        operation_sym = input("Pick an operations: ")
        calculation_func = operations[operation_sym]
        answer = calculation_func(num1, num2)
        print(f"{num1}{operation_sym}{num2} = {answer}")

        keep_cal = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.").lower()
        if keep_cal == "y":
            num1 = answer
        elif keep_cal == "n":
            should_continue = False
            calculator()


calculator()
