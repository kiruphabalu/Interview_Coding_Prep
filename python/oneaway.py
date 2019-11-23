def oneaway(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    count = 0
    if sorted(str1) == sorted(str2):
        return True
    for i in sorted_str2:
        if i not in sorted_str1:
            count+=1
    if count>1:
        return False
    else:
        return True

string1 = 'pale'
string2 = 'bale'

result = oneaway(string1, string2)
print result
