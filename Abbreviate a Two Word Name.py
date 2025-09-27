def abbrev_name(name):
    words = list(name.split(" "))
    abbreviated = [ x[0].upper() for x in words ]
    return ".".join(abbreviated)

print(abbrev_name("Sam Harris"))