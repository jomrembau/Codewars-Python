import math

def persistence(n):
    str_list = [int(d) for d in str(n)]
    repetition = 0
    while len(str_list) > 1:
        str_list = [int(d) for d in str(math.prod(str_list))]
        repetition += 1

    return repetition

print(persistence(39))