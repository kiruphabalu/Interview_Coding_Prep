def getfactorial(n):
    if n == 1:
        return 1
    else:
        return (n * getfactorial(n-1))

def getfactorial_iter(n):
    result = 1
    for x in range(1,n):
        result = result*(x+1)
    print result

print getfactorial(5)
getfactorial_iter(5)
