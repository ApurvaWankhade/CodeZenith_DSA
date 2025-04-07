def bucketSort(arr):
    if not arr:
        return arr
    
    bucket_count = len(arr)
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / bucket_count
    buckets =[[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    return [num for bucket in buckets for num in bucket]


# Example Usage
data = [64, 34, 25, 12, 22, 11, 90]
print("Bucket Sort:", bucketSort(data[:]))

