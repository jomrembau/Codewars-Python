def delete_nth(order, max_e):
    res = []
    for x in order:
        if res.count(x) < max_e:
            res.append(x)
    return res

print(delete_nth([20, 37, 20, 21], 1))