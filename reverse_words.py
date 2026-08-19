def reverse_words(text):
    x = text.split()
    reversed_list = []
    for i in x:
        reversed_list.append(i[::-1])

    return " ".join(reversed_list)

print(reverse_words("Python is fun"))