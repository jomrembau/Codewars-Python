def unique_in_order(sequence):
    new_list = []
    if len(sequence) == 0:
        return []
    else:
        new_list.append(sequence[0])
        for x in range(1,len(sequence)):
            if sequence[x] != sequence[x-1]:
                new_list.append(sequence[x])
    return new_list


print(unique_in_order("AAAABBBCCDAABBB"))