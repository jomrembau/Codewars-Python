def increment_string(string):
    num_list = []
    new_list = []
    for x in string:
        try:
            num_list.append(int(x))
        except ValueError:
            new_list.append(x)
    if len(num_list) > 0:
        to_combine = [str(i) for i in num_list]
        whole_number = int("".join(to_combine))
        new_list.append(str(whole_number + 1))
        return "".join(new_list)
    else:
        return f'{"".join(new_list)}1'

print(increment_string("foo"))