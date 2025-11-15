def expanded_form(num):
    str_num = str(num)
    zeroes = len(str_num) -1
    second_zeroes = len(str_num) -1
    final_list = []
    for x in str_num:
        if x == "0":
            zeroes -= 1
            second_zeroes = second_zeroes - 1
        else:
            while zeroes != 0:
                x = x + "0"
                zeroes -= 1
            zeroes = second_zeroes - 1
            second_zeroes = second_zeroes - 1
            final_list.append(x)
    return " + ".join(final_list)


print(expanded_form(70304))
