def add_length(str_):
    str_ = [ x + f" {len(x)}" for x in str_.split()]
    return str_

print(add_length('apple ban'))