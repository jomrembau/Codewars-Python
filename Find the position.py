import string

alphabet = list(string.ascii_lowercase)

def position(letter):
    return f"Position of alphabet: {alphabet.index(letter) + 1}"

print(position("a"))



