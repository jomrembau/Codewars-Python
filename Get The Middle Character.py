def get_middle(s):
    if len(s) % 2 == 0:
        mid = int(len(s) / 2)
        return f"{s[mid - 1]}{s[mid]}"
    if len(s) % 2 == 1:
        mid = int(len(s) / 2)
        return s[mid]

print(get_middle("tests"))