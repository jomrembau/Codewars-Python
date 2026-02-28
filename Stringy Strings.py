def stringy(size):
    stringy_list = []
    while len(stringy_list) < size:
        stringy_list.append("1")
        stringy_list.append("0")
    return "".join(stringy_list[0:size])

print(stringy(5))