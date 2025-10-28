def summation(num):
    num_list = []
    for x in range(1,num+1):
        num_list.append(x)
    return sum(num_list)


print(summation(8))