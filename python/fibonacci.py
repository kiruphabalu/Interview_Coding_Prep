def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def fibonacci_iter(n):
    fibonacci_array = []
    for x in range(0,n):
        if x<=1:
            fibonacci_array.append(x)
        else:
            result = fibonacci_array[x-1] + fibonacci_array[x-2]
            fibonacci_array.append(result)
    print fibonacci_array

for x in range(0,9):
    print(fibonacci(x))
fibonacci_iter(9)
