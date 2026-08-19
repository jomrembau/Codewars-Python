def sum_positive(numbers):
    positive_sum = [ x for x in numbers if x > 0]
    return sum(positive_sum)


print(sum_positive([5, -2, 10, -7, 3, 0]))