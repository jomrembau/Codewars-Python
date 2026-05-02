def multiply(a,b):
    return a * b

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def divide(a,b):
    return a / b

def arithmetic(a, b, operator):
    return operator(a,b)

print(arithmetic(2,2,divide))