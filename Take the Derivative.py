def derive(coefficient, exponent):
    result = str(coefficient*exponent)

    if exponent < 2:
        return result + "x^"
    else:
        return f"{result}x^{exponent-1}"

print(derive(7,8))