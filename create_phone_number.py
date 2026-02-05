def create_phone_number(n):
    stringed = [str(x) for x in n]
    return f'({"".join(stringed[0:3])}) {"".join(stringed[3:6])}-{"".join(stringed[6::])}'

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))