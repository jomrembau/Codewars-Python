def solution(string):
    str_list = list(string)
    return "".join(str_list[::-1])

print(solution("world"))