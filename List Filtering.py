
current_list = [23,12,"zu", 4,1,"iol,45"]

def filter_list(l):
    new_list = []
    for x in l:
        if isinstance(x, int):
            new_list.append(x)
    return sorted(new_list)

print(filter_list(current_list))

