sentence_check = "HELLO WQORLD  "

def generate_hashtag(s):
    new_list = []
    num_of_char = []
    for x in s:
        num_of_char.append(x)
    if len(num_of_char) == 0:
        return False
    else:
        new_list.append("#")
        split_words = s.split()
        for x in split_words:
            x = x.capitalize()
            new_list.append(x)

    if len("".join(new_list)) > 140:
        return False
    else:
        return "".join(new_list)

print(generate_hashtag(sentence_check))