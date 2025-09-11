def get_sum(a,b):
    sum_total = 0
    if a <= b:
        for x in range (a,b+1):
            sum_total += x
        return sum_total
    else:
        for x in range (b,a+1):
            sum_total += x
        return sum_total

print(get_sum(4,-1))