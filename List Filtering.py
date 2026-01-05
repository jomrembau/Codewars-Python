
current_list = [23,12,"zu", 4,1,"iol,45"]

def filter_list(l):
    new_list = []
    for x in l:
        if type(x) == int:
            new_list.append(x)
    return new_list

print(filter_list(current_list))

