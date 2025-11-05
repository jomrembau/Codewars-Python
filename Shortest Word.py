


def find_short(s):
    s = s.split()
    current_word = 100
    for word in s:
        if len(word) <= current_word:
            current_word = len(word)
    return current_word

print(find_short("bitcoin take over the world maybe who knows perhaps"))