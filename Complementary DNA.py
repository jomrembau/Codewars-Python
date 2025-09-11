

def DNA_strand(dna):
    new_list = []
    for x in dna:
        if x == "A":
            y = "T"
            new_list.append(y)
        if x == "T":
            y = "A"
            new_list.append(y)
        if x == "G":
            y = "C"
            new_list.append(y)
        if x == "C":
            y = "G"
            new_list.append(y)
    return ''.join(new_list)


print(DNA_strand("AAAA"))