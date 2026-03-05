def is_divisible(*args):
    for x in args:
        if args[0] % x != 0:
            return False
    return True

print(is_divisible(3,3,4))