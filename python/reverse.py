def reverse_string(string):
    reversedstring = []
    length = len(string)
    while length >0:
        reversedstring += string[length -1]
        length -=1

    print (reversedstring)

reverse_string('kirupha')        
