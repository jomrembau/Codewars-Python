def are_you_playing_banjo(name):
    letter_list = [x.lower() for x in name]
    if letter_list[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"



print(are_you_playing_banjo("martin"))
