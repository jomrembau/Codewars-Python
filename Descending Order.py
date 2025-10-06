def descending_order(num):
    num_list = [ int(x) for x in str(num)]
    num_list.sort(reverse=True)
    final_list = [str(x) for x in num_list]
    return int("".join(final_list))

print(descending_order(123456789))