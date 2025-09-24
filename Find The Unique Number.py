from collections import Counter

def find_uniq(arr):
    counts = Counter(arr)
    for num, count in counts.items():
        if count == 1:
            return num

print(find_uniq([3, 10, 3, 3, 3]))