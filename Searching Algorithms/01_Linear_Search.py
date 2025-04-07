def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

data = [1, 3, 5, 7, 9, 11, 15, 18, 20]
target = 7
print("Linear Search:", linearSearch(data, target))