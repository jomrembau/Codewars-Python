def reverse_letter(st):
    new_list = [ x for x in st if x.isalpha()  ]
    return "".join(reversed(new_list))

print(reverse_letter("ultr53o"))
