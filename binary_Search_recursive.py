def binary_search(ls, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    if ls[mid] == target:
        return mid
    if ls[mid] > target:
        return binary_search(ls, target, low, mid - 1)
    else:
        return binary_search(ls, target, mid + 1, high)


ls1 = [1, 5, 7, 18, 85, 102]
index = binary_search(ls1, 18, 0, len(ls1) - 1)
if index == -1:
    print("Target not found")
else:
    print(index)

