def fibonacciSearch(arr, target):
    n = len(arr)
    fib2, fib1 = 0, 1
    fib = fib2 + fib1
    
    while fib < n:
        fib2, fib1 = fib1, fib
        fib = fib2 + fib1
    
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < target:
            fib, fib1, fib2 = fib1, fib2, fib - fib1
            offset = i
        elif arr[i] > target:
            fib, fib1, fib2 = fib2, fib1 - fib2, fib - fib1
        else:
            return i
    
    if fib1 and arr[offset + 1] == target:
        return offset + 1
    return -1

data = [1, 3, 5, 7, 9, 11, 15, 18, 20]
target = 7
print("Fibonacci Search:", fibonacciSearch(data, target))