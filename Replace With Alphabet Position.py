Input = "The sunset sets at twelve o' clock."

alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def alphabet_position(text):
    new_list = []
    for x in text:
        x = x.lower()
        if x not in alpha_list:
            pass
        else:
            position = str(alpha_list.index(x) + 1)
            new_list.append(position)
    return " ".join(new_list)

print(alphabet_position(Input))