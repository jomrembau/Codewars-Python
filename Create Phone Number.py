

def create_phone_number(n):

    new_list = []
    for x in n:
        a = str(x)
        new_list.append(a)

    vorwahl = list(new_list[:3])
    mid_3 = list(new_list[3:6])
    last_4 = list(new_list[-4:])

    return f'({"".join(vorwahl)}) {"".join(mid_3)}-{"".join(last_4)}'

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))