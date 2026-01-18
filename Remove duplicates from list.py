def distinct(seq):
    new_list = []
    for x in seq:
        if x not in new_list:
            new_list.append(x)
    return new_list