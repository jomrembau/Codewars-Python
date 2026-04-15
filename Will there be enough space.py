def enough(cap, on, wait):
    free_seats = cap - on
    if free_seats >= wait:
        return 0
    else:
        return (on + wait) - cap

print(enough(100, 60, 50))