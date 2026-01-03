def is_uppercase(inp):
    for x in inp:
        if x.islower():
            return False
        continue
    return True

print(is_uppercase("9ais0d~tC8["))