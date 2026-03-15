def rental_car_cost(d):
    if 6 < d:
        return (d * 40) - 50
    elif 3 <= d <= 6:
        return (d * 40) - 20
    else:
        return d * 40

print(rental_car_cost(110))