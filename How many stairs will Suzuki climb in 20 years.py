def stairs_in_20(stairs):
    total_stairs = 0
    for x in stairs:
        total_stairs = total_stairs + sum(x)

    return 20 * total_stairs
