def cakes(recipe, available):
    rec_list = []
    available_list = available.keys()
    for x in recipe:
        if x not in available_list:
            return 0
        rec1 = available[x] // recipe[x]
        rec_list.append(rec1)
    return min(rec_list)

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))