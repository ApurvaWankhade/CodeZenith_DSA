def countinf_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(n-1,-1,-1):
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = output[i]


def radixSort(arr):
    if not arr:
        return arr
    max_num  = max(arr)
    exp = 1
    while max_num // exp > 0:
        countinf_sort_exp(arr, exp)
        exp *= 10

    return arr

# Example Usage
data = [64, 34, 25, 12, 22, 11, 90]
print("Radix Sort:", radixSort(data[:]))

