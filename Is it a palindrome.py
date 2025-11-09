def is_palindrome(s):
    s = [x.lower() for x in s]
    if s == s[::-1]:
        return True
    else:
        return False


print(is_palindrome("kodok"))