def nb_dig(n, d):
    squared_list = []
    count = 0
    for x in range(0,n+1):
        squared = x * x
        squared_list.append(str(squared))
    for i in squared_list:
        d_count = i.count(str(d))
        count = count + d_count
    return count


print(nb_dig(10,1))