def rot13(message):
    shift = 13 % 26
    new_list = []
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            new_list.append(new_char)
        else:
            new_list.append(char)

    return ''.join(new_list)

print(rot13("test"))