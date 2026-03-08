def title_case(title, minor_words=''):
    words = title.split()
    minor_words = minor_words.split()
    words = [x.lower() for x in words]
    minor_words = [x.lower() for x in minor_words]
    new_list = []
    if title:
        new_list.append(words[0].title())
    for x in range(1, len(words)):
        if words[x] in minor_words:
            new_list.append(words[x].lower())
        else:
            new_list.append(words[x].title())
    return " ".join(new_list)


print(title_case('THE WIND IN THE WILLOWS', 'The In'))