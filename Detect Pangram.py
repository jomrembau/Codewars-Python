sentence = "The quick brown fox jumps over the lazy dog"

def is_pangram(st):
    letters_list = []
    for x in st:
        if x.isalpha():
            x = x.lower()
            if x not in letters_list:
                letters_list.append(x)
        else:
            pass

    if len(letters_list) == 26:
        return True
    else:
        return False

print(is_pangram(sentence))



