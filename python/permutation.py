def permutation (string1, string2):
    if len(string1) != len(string2):
        return False
    print sorted(string2)
    if sorted(string1) == sorted(string2):
        print 'True'
    ret = True
    for i in string1:
        if i not in string2:
            ret = False
            break
    return ret

string1 = 'kirupha'
string2 = 'acb'

result = permutation(string1, string2)
print (result)
