def gimme(input_array):
    new_list = [x for x in input_array]
    new_list.remove(min(input_array))
    new_list.remove(max(input_array))
    return input_array.index(new_list[0])

print(gimme([2, 3, 1]))