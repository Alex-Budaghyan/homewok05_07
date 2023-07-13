def fibonacci(n, fib_cache = {}):
    if type(n) is not int:
        raise ValueError("n must be integer")

    if n in fib_cache:
        return fib_cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 2) + fibonacci(n - 1)

    fib_cache[n] = result
    return result


try:
    print(fibonacci(11))
except ValueError as ve:
    print(str(ve))
