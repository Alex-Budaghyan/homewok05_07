def binary_search(ls, target):
    low = 0
    high = len(ls) - 1
    while low <= high:
        mid = (low + high) // 2
        if ls[mid] == target:
            return mid
        if ls[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


ls1 = [1, 2, 8, 9, 15, 54, 96, 102]
index = binary_search(ls1, 96)
if index == -1:
    print("target not found")
else:
    print(index)