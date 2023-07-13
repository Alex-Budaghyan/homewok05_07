def selection_sort(array: list) -> list:
    try:
        array = list(array)
    except TypeError:
        raise TypeError("Array is not a list and can't be casted to list")
    try:
        for i in range(len(array)):
            min_index = array.index(min(array[i:]))
            array[i], array[min_index] = array[min_index], array[i]
    except TypeError:
        raise TypeError("The types are incomparable")
    return array


ls1 = [1, 5, 7, 9, 3, 4, 2, 8]

try:
    print(selection_sort(ls1))
except TypeError as t:
    print(str(t))
