def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    positive_count = 0
    sum_negative = []
    for x in arr:
        if x == 0:
            pass
        if x > 0:
            positive_count += 1
        if x < 0:
            sum_negative.append(x)
    new_list = [positive_count, sum(sum_negative)]

    if positive_count == 0 and sum(sum_negative) == 0:
        return [0,0]
    else:
        return new_list


print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))