x = [1, 2, 2, 2, 3]
y = [2]

def array_diff(a, b):
    new_list = []
    for number in a:
        if number not in b:
            new_list.append(number)
    return new_list


print(array_diff(x,y))
