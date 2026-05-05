def multiplication_table(size):
    muliplication_list = []
    add_list = []

    repetition = 1

    while repetition <= size:
        for x in range(1,size+1):
            add_list.append(repetition * x)
        repetition += 1
        muliplication_list.append(add_list)
        add_list = []

    return muliplication_list

print(multiplication_table(3))