import re

def high_and_low(numbers):
    int_list = [int(s) for s in re.findall(r'-?\d+', numbers)]
    return f"{max(int_list)} {min(int_list)}"

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))