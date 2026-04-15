def array(string):
    if string == "":
        return None
    string = string.split(",")
    if " ".join(string[1:-1]) == "":
        return None
    else:
        return " ".join(string[1:-1])


print((array('1,2,3')))