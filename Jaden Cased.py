

quote = "How can mirrors be real if our eyes aren't real"

def to_jaden_case(string):
    new_quote = []
    for i in string.split():
       new_quote.append(i.capitalize())
    return " ".join(new_quote)

print(to_jaden_case(quote))