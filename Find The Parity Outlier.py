def find_outlier(integers):
    even_count = []
    odd_count = []
    for x in integers:
        if x % 2 == 0:
            even_count.append(x)
        else:
            odd_count.append(x)
    if len(even_count) < len(odd_count):
        return even_count[0]
    else: return odd_count[0]

print(find_outlier([2, 4, 6, 8, 10, 3]))