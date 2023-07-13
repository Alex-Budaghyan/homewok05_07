def insertion_sort(array: list) -> list:
    try:
        array = list(array)
    except TypeError:
        raise TypeError("Array is not a list and can't be casted to list")

    index = 0
    while index < len(array) - 1:
        try:
            i = index
            while array[i] > array[i + 1] and i >= 0:
                array[i], array[i + 1] = array[i + 1], array[i]
                i -= 1
            index += 1
        except TypeError:
            raise TypeError("The types are incomparable")
    return array


ls1 = [1, 5, 7, 9, 3, 4, 2, 8]


try:
    print(insertion_sort(ls1))
except TypeError as t:
    print(str(t))

