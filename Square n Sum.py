to_square = [1, 2, 2]

def square_sum(numbers):
    new_list = []
    for x in numbers:
        squared = x * x
        new_list.append(squared)
    return sum(new_list)

print(square_sum(to_square))
