def is_anagram(test, original):

    a = [x.lower() for x in test]
    b = [x.lower() for x in original]
    if sorted(a) == sorted(b):
        return True
    else:
        return False

print(is_anagram("foefet", "toffee"))