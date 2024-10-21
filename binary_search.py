def binary_search(arr, value):
    "Алгоритм бинарного поиска."
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        item = arr[middle]
        if item < value:
            left = middle + 1
        elif item > value:
            right = middle - 1
        elif item == value:
            return middle
    return None


if __name__ == "__main__":
    arr = [2, 3, 4, 5]
    value = 2
    print(binary_search(arr, value))
