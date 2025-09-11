test = [0,0,1,0]

def binary_array_to_number(arr):
    multiply_by = 1
    whole_num = 0
    corrected_list = [x for x in arr[::-1]]
    for i in corrected_list:
        to_add= i * multiply_by
        whole_num += to_add
        multiply_by *= 2
    return whole_num

print(binary_array_to_number(test))


