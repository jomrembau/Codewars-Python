import math

def is_square(n):
    if n < 0:
        return False
    else:
        n = math.sqrt(n)
        if n.is_integer():
            return True
        else:
            return False

print(is_square(0))
