def bouncing_ball(h, bounce, window):
    fall_and_bounce = 0
    if h > 0 and (0 < bounce < 1) and window < h:
        while h > window:
            fall_and_bounce += 1
            h = h * bounce
            if h > window:
                fall_and_bounce += 1
    else:
        return -1
    return fall_and_bounce


print(bouncing_ball(2, 0.5, 1)) 
