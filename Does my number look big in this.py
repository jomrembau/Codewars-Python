def narcissistic( value ):
    stringed = str(value)
    raise_to = len(stringed)
    final_list = []
    num_list = [ int(x) for x in stringed]
    for i in num_list:
        b = i ** raise_to
        final_list.append(b)
    if sum(final_list) == value:
        return True
    else:
        return False



print(narcissistic(7))