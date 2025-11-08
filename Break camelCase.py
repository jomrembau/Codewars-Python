def solution(s):
    new_list = []
    for char in s:
        if char == char.lower():
            new_list.append(char)
        else:
            new_list.append(f" {char.upper()}")
    return "".join(new_list)


print(solution("helloWorld"))