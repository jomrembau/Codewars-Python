def array_diff(a, b):
    difference = [x for x in a if x not in b]
    return difference

print(array_diff([1,2], [1]) )