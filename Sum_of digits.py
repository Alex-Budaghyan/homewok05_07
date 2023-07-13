def sum_of_digits(num):
    if type(num) is not int:
        raise ValueError("Num must be integer")

    if num < 10:
        return num
    else:
        return num % 10 + sum_of_digits(num // 10)


try:
    print(sum_of_digits(178561))
except ValueError as ve:
    print(str(ve))
