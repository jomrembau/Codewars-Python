import math

def find_next_square(sq):
    to_find = True
    current_sq = math.isqrt(sq)
    target_sq = current_sq + 1
    if current_sq * current_sq != sq:
        return -1

    while to_find:
        sq += 1
        incremental = sq ** 0.5
        if incremental == target_sq:
            to_find = False

    return sq

print(find_next_square(155))