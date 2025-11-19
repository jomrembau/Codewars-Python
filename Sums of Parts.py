def parts_sums(ls):
    total = sum(ls)
    final_list = [total]
    for x in ls:
        total -= x
        final_list.append(total)
    return final_list

print(parts_sums([0, 1, 3, 6, 10]))