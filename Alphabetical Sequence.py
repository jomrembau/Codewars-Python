import string

alphabet_list = list(string.ascii_lowercase)


def alpha_seq(strng):
    final_list = []
    strng = [x.upper() for x in strng]
    for char in strng:
        char = char.lower()
        current_letter = char
        to_print = alphabet_list.index(char)
        char = char.upper()
        while to_print > 0:
            char = char + current_letter
            to_print -= 1
        final_list.append(char)

    return ",".join(sorted(final_list))

print(alpha_seq("BfcFA"))

