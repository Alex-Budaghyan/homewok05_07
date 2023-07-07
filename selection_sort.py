def selection_sort(array: list) -> list:
    for i in range(len(array)):
        small = min(array[i:])
        index_small = array.index(small)
        array[i], array[index_small] = array[index_small], array[i]
    return array


arr = [1, 5, 7, 8, 3, 4, 9, 6, 2]
print(selection_sort(arr))