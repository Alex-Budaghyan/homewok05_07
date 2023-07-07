def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return arr


arr1 = [1, 8, 4, 5, 9, 6, 3, 7, 2]
print(bubble_sort(arr1))
