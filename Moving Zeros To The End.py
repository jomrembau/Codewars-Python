def move_zeros(lst):
    new_list = []
    zero_count = 1
    for x in lst:
        if x != 0:
            new_list.append(x)
        else:
            zero_count += 1

    for i in range(1,zero_count):
        new_list.append(0)

    return new_list

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))