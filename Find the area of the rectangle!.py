def area(d, l):
    if d <= l:
        return "Not a rectangle"
    else:
        w = ((d*d) - (l*l)) ** 0.5
        return round((w * l),2)

print(area(5, 4))