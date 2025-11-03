def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    new_list = list(numbers)
    new_list.remove(min(new_list))
    return new_list

print(remove_smallest([1, 2, 3, 4, 5]))