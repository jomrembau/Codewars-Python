import string

input = "hello"

alphabet_list = list(string.ascii_lowercase)

def wave(people):
    new_list = []
    for x in range(0,len(people)):
        new_word = []
        if people[x] not in alphabet_list:
            pass
        else:
            big_letter = people[x].upper()
            for i in range(0, len(people)):
                if i == x:
                    new_word.append(big_letter)
                else:
                    new_word.append(people[i])
            word_to_add = "".join(new_word)
            new_list.append(word_to_add)
    return new_list

print(wave(input))