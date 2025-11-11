def divisors(integer):
    divisor_list = []
    for x in range(2,integer):
        if integer % x == 0:
            divisor_list.append(x)
    if len(divisor_list) == 0:
        return f"{integer} is prime"
    else:
        return divisor_list


print(divisors(15))