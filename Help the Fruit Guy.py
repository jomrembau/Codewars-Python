def remove_rotten(bag_of_fruits):
    if not bag_of_fruits:
            return []

    fresh_list = []
    for x in bag_of_fruits:
        x = x.lower()
        if "rotten" in x:
            fresh_list.append(x.replace("rotten",""))
        else:
            fresh_list.append(x.lower())


    return fresh_list

print(remove_rotten(["apple","rottenBanana","apple"]))