def string_expansion(s):
    s = [x for x in s]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    final_list = []
    current = 1
    for x in s:
        if x not in numbers:
            final_list.append(x * current)
        else:
            current = int(x)
            continue

    return "".join(final_list)

print(string_expansion("3D2a5d2f"))