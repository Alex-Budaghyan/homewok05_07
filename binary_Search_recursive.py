class TargetNotFoundException(Exception):
    pass


def binary_search_recursive(array, target, low, high):
    try:
        target = float(target)
    except ValueError:
        raise ValueError("Target is not a valid number")

    try:
        if low > high:
            raise TargetNotFoundException("Target not found in the list")
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search_recursive(array, target, low, mid - 1)
        else:
            return binary_search_recursive(array, target, mid + 1, high)
    except Exception:
        raise TargetNotFoundException("Target not found in the list")


ls1 = [1, 2, 4, 25, 64, 78]

try:
    print(binary_search_recursive(ls1, 25, 0, len(ls1) - 1))
except ValueError as v:
    print(str(v))
except TargetNotFoundException as t:
    print(str(t))
