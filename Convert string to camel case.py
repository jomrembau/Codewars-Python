to_convert = "the-stealth-warrior"

symbols = "!\"§$%&/()=?`´^°*'+#'-_.:,;<>|@€"

def to_camel_case(text):
    capitalized_list = []
    for s in symbols:
        text = text.replace(s, " ")
    new_list = list( text.split())

    if not new_list:
        return ""

    for x in range(1,len(new_list)):
        capitalized_word = new_list[x].capitalize()
        capitalized_list.append(capitalized_word)

    return new_list[0] + "".join(capitalized_list)



print(to_camel_case(to_convert))
