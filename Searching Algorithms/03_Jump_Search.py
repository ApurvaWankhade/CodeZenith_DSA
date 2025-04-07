def jumpSearch(arr, target):
    import math
    n = len(arr)
    step = int(math.sqrt(n))
    prev, curr = 0, 0
    
    while curr < n and arr[curr] < target:
        prev = curr
        curr += step
    
    for i in range(prev, min(curr, n)):
        if arr[i] == target:
            return i
    return -1

data = [1, 3, 5, 7, 9, 11, 15, 18, 20]
target = 7
print("Jump Search:", jumpSearch(data, target))