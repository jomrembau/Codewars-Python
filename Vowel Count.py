

def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for x in sentence:
        if x in vowels:
            vowel_count += 1
    return vowel_count