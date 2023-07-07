def insertion_sort(array: list) -> list:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = key
    return array


arr1 = [1, 5, 6, 4, 7, 3, 9, 8, 2]
print(insertion_sort(arr1))


