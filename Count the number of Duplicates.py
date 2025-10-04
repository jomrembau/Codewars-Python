def duplicate_count(text):
    new_list = []
    done = []
    if text == "":
        return 0
    for x in text:
        if x.isalpha():
            x = x.lower()
            new_list.append(x)
        else:
            new_list.append(x)

    for i in new_list:
        if i not in done:
            if new_list.count(i) >= 2:
                done.append(i)

    return len(done)

print(duplicate_count("abcdeaB"))
