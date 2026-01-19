def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


print(find_average([1, 2, 3]))