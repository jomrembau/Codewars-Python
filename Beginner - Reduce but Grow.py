def grow(arr):
    arr = sorted(arr)
    current = 1
    for x in arr:
        current = x * current
    return current

print(grow([4, 1, 1, 1, 4]))