def find_largest(numbers):
    largest_number = numbers[0]

    for i in numbers:
        if i > largest_number:
            largest_number = i

    return largest_number

print(find_largest([4, 12, 7, 31, 9]))