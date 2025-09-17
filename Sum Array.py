

initial_input = [1, 5.2, 4, 0, -1]


def sum_array(a):
    new_list = []
    for x in a:
        new_list.append(float(x))
    return sum(new_list)

print(sum_array(initial_input))