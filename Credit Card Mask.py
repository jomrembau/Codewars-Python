string1 = "4556364607935616"

def maskify(cc):
    new_list = []
    masked =[]
    for x in cc:
        new_list.append(x)

    for i in range(0,len(new_list)-4):
        masked.append("#")

    to_show = new_list[-4:]

    return "".join(masked)   + "".join(to_show)


print(maskify(string1))



