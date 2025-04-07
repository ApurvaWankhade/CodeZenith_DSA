def binarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
 
data = [1, 3, 5, 7, 9, 11, 15, 18, 20]
target = 7
print("Binary Search:", binarySearch(data, target))