likers = ["Alex", "Jacob", "Mark", "Max"]


def likes(names):
    if len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) > 3:
        other_likes = len(names) - 2
        return f"{names[0]}, {names[1]} and {other_likes} others like this"
    else:
        return "no one likes this"


print(likes(likers))