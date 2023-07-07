def factorial(num ,fact_cache = {}):
    if num == 0 or num == 1:
        return 1
    if num in fact_cache:
        return fact_cache[num]
    if num < 0:
        raise ValueError("The number can't be negative")
    res = factorial(num - 1) * num
    fact_cache[num] = res
    return res


print(factorial(5))
print(factorial(14))
