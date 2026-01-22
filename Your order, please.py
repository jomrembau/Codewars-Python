def order(sentence):
    new_list = []
    sentence = sentence.split()
    for x in range(1,len(sentence) +1):
        for i in sentence:
            if str(x) in i:
                new_list.append(i)
    return " ".join(new_list)

print(order("is2 Thi1s T4est 3a"))