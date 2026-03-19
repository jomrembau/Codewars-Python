def duty_free(price, discount, holiday_cost):
    return int(holiday_cost / round(price * (discount * .01),2))

print(duty_free(12, 50, 1000))