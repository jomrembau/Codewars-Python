def square_digits(num):
    str_num = str(num)
    num_list = [int(x) for x in str_num]
    final_list = []
    for x in num_list:
        m = x * x
        final_list.append(str(m))
    return int("".join(final_list))

print(square_digits(9119))