def invert(lst):
    new_list = []
    for x in lst:
        if len(lst) == 0 or x == 0:
            new_list.append(0)
        elif x > 0 :
            new_list.append(-abs(x))
        elif x < 0 :
            new_list.append(abs(x))

    return new_list


print(invert([1, 2, 3, 4, 5] ))