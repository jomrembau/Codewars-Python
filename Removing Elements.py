def remove_every_other(my_list):
    final_list = []
    for x in range(0, len(my_list), 2):
        final_list.append(my_list[x])
    return final_list

print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))

