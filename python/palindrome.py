def is_palindrome(s):
    print s[1:-1]
    length = len(s)
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

a = 'madam'
b = is_palindrome(a)
print b
