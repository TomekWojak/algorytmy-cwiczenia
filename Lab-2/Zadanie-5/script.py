def binary_search(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)


arr = [2, 5, 8, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
target = 55

result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Znaleziono. Indeks elementu:", result)
else:
    print("Nie znaleziono")