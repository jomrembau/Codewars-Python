
def xo(s):
    new_list = [ x.lower() for x in s]
    x_count = 0
    o_count = 0
    for i in new_list:
        if i == "x":
            x_count += 1
        elif i == "o":
            o_count += 1
        else:
            pass
    if x_count == o_count:
        return True
    else:
        return False
