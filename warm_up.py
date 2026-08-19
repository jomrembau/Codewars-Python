def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count+=1
    return count

print(count_even([3, 8, 12, 5, 7, 20]))