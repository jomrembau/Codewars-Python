import string

def alphanumeric(password: str) -> bool:

    if not password:
        return False
    for x in password:
        if x in string.punctuation or x in string.whitespace:
            return False
    return True
