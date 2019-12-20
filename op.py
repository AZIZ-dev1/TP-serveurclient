def add(a, b):
    return a + b  # Cette fonction donne l'addition de deux nombres


def sub(a, b):    # Cette fonction donne la soustraction de deux nombres
    return a - b


def mul(a, b):     # Cette fonction donne la multiplication de deux nombres
    return a * b


def div(a, b):   # Cette fonction donne la division d'un nombre par un nombre non-zero 
    if b==0 :return "Division by zero is disallowed."
    else: return a / b

def divrem(a, b):  # Cette fonction donne le rest d'une division
    return a % b
