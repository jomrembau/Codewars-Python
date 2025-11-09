def powers_of_two(n):
    new_list = []
    for x in range(0,n+1):
        new_list.append(2**x)

    return new_list

print(powers_of_two(4))