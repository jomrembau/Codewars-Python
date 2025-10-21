def fake_bin(x):
    new_list = [int(char) for char in x]
    binary = []
    for i in new_list:
        if i >= 5:
            binary.append(str(1))
        else: binary.append(str(0))
    return "".join(binary)
