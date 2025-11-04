def count(s):
    if s == {}:
        return {}
    final_count = {}
    for char in s:
        final_count[char] = s.count(char)
    return final_count

print(count("aba"))