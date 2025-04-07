def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left_arr = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right_arr = [x for x in arr if x > pivot]

    return quickSort(left_arr) + middle + quickSort(right_arr)

# Example Usage
data = [64, 34, 25, 12, 22, 11, 90]
print("Quick Sort:", quickSort(data[:]))





