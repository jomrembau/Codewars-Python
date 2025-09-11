name_list = ["Ryan", "Kieran", "Jason", "Yous"]


def friend(x):
    friends_list = []
    for name in x:
        if len(name) == 4 and name not in friends_list:
            friends_list.append(name)
    return friends_list

print(friend(name_list))


