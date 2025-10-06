def count_by(x, n):
    new_list = []
    total = 0
    while len(new_list) < n:
        total += x
        new_list.append(total)
    return new_list

print(count_by(2, 5))