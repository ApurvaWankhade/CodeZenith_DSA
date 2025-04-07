def heapSort(arr):
    import heapq
    heapq.heapify(arr)

    return [heapq.heappop(arr) for _ in range(len(arr))]

# Example Usage
data = [64, 34, 25, 12, 22, 11, 90]
print("Heap Sort:", heapSort(data[:]))

