def digital_root(n):
    n = str(n)
    n = [x for x in n]
    n = [int(x) for x in n]
    if sum(n) < 10:
        return sum(n)
    else:
        return digital_root((sum(n)))

print(digital_root(493193))