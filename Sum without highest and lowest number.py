def sum_array(arr):
    try:
        if len(arr) < 2:
            return 0
        arr.remove(min(arr))
        arr.remove(max(arr))
        return sum(arr)
    except:
        return 0

print(sum_array([6, 0, 1, 10, 10]))