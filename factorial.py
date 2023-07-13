def factorial(num, fact_cache = {}):
    if type(num) is not int:
        raise ValueError("Number must be integer")

    if num in fact_cache:
        return fact_cache[num]
    if num == 0 or num == 1:
        result = 1
    elif num < 0:
        raise ValueError("The number can't be negative")
    else:
        result = factorial(num - 1) * num
    fact_cache[num] = result
    return result


try:
    print(factorial(15))
except ValueError as ve:
    print(str(ve))
