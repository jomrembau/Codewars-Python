def solution(number):
    num_list = []
    if number < 3:
        return 0
    multiple_3 = 3
    multiple_5 = 5
    while multiple_3 < number:
        num_list.append(multiple_3)
        multiple_3 += 3
    while multiple_5 < number:
        num_list.append(multiple_5)
        multiple_5 += 5
    num_set = set(num_list)
    return sum(list(num_set))


print(solution(6))