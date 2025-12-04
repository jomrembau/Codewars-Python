def sort_by_length(arr):
    liste = {}

    for x in arr:
        liste[x] = len(x)
    sorted_values =  dict(sorted(liste.items(), key=lambda item: item[1]))
    final_list = [keys for keys in sorted_values]
    return final_list

print(sort_by_length(["", "pizza", "brains", "moderately"]))