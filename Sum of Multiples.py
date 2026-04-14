def sum_mul(n, m):
    total_sum = 0

    if n <= 0 or m <= 0:
        return "INVALID"

    for x in range ( n,m,n):
        total_sum += x
    return total_sum


print(sum_mul(2,9))