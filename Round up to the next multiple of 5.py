def round_to_next5(n):
    continue_calculate = True
    while continue_calculate:
        if n % 5 == 0:
            return n
        else: n += 1

print(round_to_next5(6))