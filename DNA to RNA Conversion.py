def dna_to_rna(dna):
    dna = [x if x != "T" else "U" for x in dna ]
    return "".join(dna)

print(dna_to_rna("GCAT"))