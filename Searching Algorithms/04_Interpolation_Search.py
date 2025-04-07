def interpolationSearch(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)// (arr[high]-arr[low]))

        if arr[pos]==target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
        
    return -1

data = [1, 3, 5, 7, 9, 11, 15, 18, 20]
target = 7
print("Interpolation Search:", interpolationSearch(data, target))