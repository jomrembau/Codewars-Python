def nb_year(p0, percent, aug, p):
    year_count = 0
    converted_percentage = percent / 100
    continue_count = True
    while continue_count:
        if p0 >= p:
            break
        additional = p0 * converted_percentage
        p0 = int(p0 + additional + aug)
        year_count += 1
    return year_count

print(nb_year(1500, 5, 100, 5000))