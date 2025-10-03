def no_space(x):
    new_list = []
    for char in x:
        if char == " ":
            pass
        else:
            new_list.append(char)
    return "".join(new_list)

print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))