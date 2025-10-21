def is_isogram(string):
    letter_list = []
    for x in string:
        x = x.lower()
        if x not in letter_list:
            letter_list.append(x)
        elif x == " ":
            continue
        else:
            return False
    return True

print(is_isogram("LxawJKTlQ"))