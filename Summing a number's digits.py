def sum_digits(number):
    number = str(abs(number))
    return sum(int(x) for x in number)

print(sum_digits(99))