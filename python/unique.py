word = 'terminology'

def unique(word):
    length = len(word)
    returnvalue = True
    for i in range(0,length):
        for j in range(i+1,length):
            if word[i] == word[j]:
                returnvalue = False
                break
    return returnvalue

result = unique(word)
print result
