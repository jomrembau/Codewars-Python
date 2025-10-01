


def printer_error(s):
    denominator = len(s)
    numerator = 0
    allowed_char = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j" ,"k" ,"l" ,"m"]

    for x in s:
        if x not in allowed_char:
            numerator += 1

    return f"{numerator}/{denominator}"


print(printer_error("aaabbbbhaijjjm"))
