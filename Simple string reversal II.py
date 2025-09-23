

def solve(st,a,b):
    new_list = list(reversed(st[a:b+1]))
    return f'{st[:a]}{"".join(new_list)}{st[b+1:]}'


print(solve("codewars",1,5))