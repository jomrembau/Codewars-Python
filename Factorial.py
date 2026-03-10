def factorial(n):
    fact = 1
    if n < 0 or n > 12:
        raise ValueError
    else:
        for x in range (1,n+1):
            fact = fact * x
    return fact

