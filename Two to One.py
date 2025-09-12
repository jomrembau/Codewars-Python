a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"


def longest(a1, a2):
    new_list = []
    for x in a1:
        if x not in new_list:
            new_list.append(x)
    for i in a2:
        if i not in new_list:
            new_list.append(i)
    new_list = sorted(new_list)

    return "".join(new_list)

print(longest(a,b))