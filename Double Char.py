def double_char(s):
    s = [x for x in s]
    new_list = []

    for char in s:
        new_list.append(char)
        new_list.append(char)

    return "".join(new_list)

print(double_char("Hello World"))