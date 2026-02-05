def find_outlier(integers):
    odd_list = []
    even_list = []
    for x in integers:
        if x % 2 == 0:
            odd_list.append(x)
        else:
            even_list.append(x)
    if len(odd_list) == 1:
        return odd_list[0]
    else: return even_list[0]

print(find_outlier([2,4,6,8,10,3]))