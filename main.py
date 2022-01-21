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

num1 = int(input("what is the first number?: "))
num2 = int(input("what is the second number?: "))

for symbl in operations:
    print(symbl)
operation_sym = input("Pick an operations from the line above: ")

calculation_func = operations[operation_sym]
answer = calculation_func(num1, num2)
print(f"{num1}{operation_sym}{num2} = {answer}")
