from collections import Counter

word1 = "Success"

def duplicate_encode(word):
    word = [ x.lower() for x in word]
    counter = Counter(word)
    counts = {key: value for key, value in counter.items() if value > 0}
    new_list = []
    for x in word:
        if counts[x] >= 2:
            new_list.append(")")
        else:
            new_list.append("(")

    print(counts)
    return ''.join(new_list)

print(duplicate_encode(word1))

