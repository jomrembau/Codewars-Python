def pig_it(text):
    word_list = text.split(" ")

    new_sentence = []

    for x in word_list:
        new_word = []
        if x in ['!', '?']:
            new_sentence.append(x)
            continue
        for i in x:
            new_word.append(i)
        new_word.append(new_word[0])
        new_word.remove(new_word[0])
        add_word = f'{"".join(new_word)}ay'
        new_sentence.append(add_word)#
    return " ".join(new_sentence)

print(pig_it('Pig latin is cool'))