def divisors(n):
    divisors = []
    for x in range(1,n + 1):
        if n % x == 0:
            divisors.append(x)
    return len(divisors)



print(divisors(12))