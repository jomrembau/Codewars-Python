def number(lines):
    final_list = []
    if not lines:
        return []

    for x in range(0,len(lines)):
        final_list.append(f"{x + 1}: {lines[x]}")

    return final_list

print(number(["a", "b", "c"]))