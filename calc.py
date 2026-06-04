import math


def root(a, b):
    return a ** (1 / b)


def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def tan(a):
    return math.tan(a)


def log(a):
    return math.log(a)


def calculate(a, b, choice):
    if choice == "1":
        return a + b
    elif choice == "2":
        return a - b
    elif choice == "3":
        return a * b
    elif choice == "4":
        return a / b
    elif choice == "5":
        return a**b
    elif choice == "6":
        return root(a, b)
    elif choice == "7":
        return factorial(a)
    elif choice == "8":
        return sin(a)
    elif choice == "9":
        return cos(a)
    elif choice == "10":
        return tan(a)
    elif choice == "11":
        return log(a)
    else:
        return None
