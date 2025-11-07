def quarter_of(month):
    month = int(month)
    quarter = 0
    if month < 4:
        quarter = 1
    elif month > 9:
        quarter = 4
    elif month >= 4 and month <= 6:
        quarter = 2
    else:
        quarter = 3
    return quarter

print(quarter_of("2"))