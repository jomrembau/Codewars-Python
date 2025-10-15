def rgb(r, g, b):
    hexa = [r,g,b]
    for i, n in enumerate(hexa):
        if n > 255:
            hexa[i] = 255
        elif n < 0:
            hexa[i] = 0

    hex_str = f'{hexa[0]:02X}{hexa[1]:02X}{hexa[2]:02X}'
    return hex_str


print(rgb(0, 128, 64))