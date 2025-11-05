def high(x):
    x = x.split()
    highest_word = ""
    current_high = 0
    for word in x:
        num_list = []
        for char in word:
            position = ord(char) - ord('a') + 1
            num_list.append(position)
            if sum(num_list) > current_high:
                current_high = sum(num_list)
                highest_word = word

    return highest_word

print(high("man i need a taxi up to ubud"))