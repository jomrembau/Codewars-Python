def flatten_and_sort(array):
    new_list = []
    for i in array:
        for x in i:
            new_list.append(x)
    return sorted(new_list)

print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))