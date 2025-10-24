def solution(s):
    new_list = [x for x in s]
    if len(s) % 2 != 0:
        new_list.append("_")

    final_list = [new_list[a]+(new_list[a+1]) for a in range(0,len(new_list),2) ]
    return final_list

print(solution("asdfadsf"))