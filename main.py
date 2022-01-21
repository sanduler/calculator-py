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
