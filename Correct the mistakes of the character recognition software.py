def correct(s):
    a = s.replace("0","O")
    b = a.replace("1","I")
    return b.replace("5","S")

print(correct("L01D05"))

