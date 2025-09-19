

def find_smallest_int(arr):
    lowest_num = arr[0]
    for x in arr:
        if x < lowest_num:
            lowest_num = x
    return lowest_num