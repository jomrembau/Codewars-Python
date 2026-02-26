def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

print(stray([1, 1, 1, 1, 1, 1, 2]))