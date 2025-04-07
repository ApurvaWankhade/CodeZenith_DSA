def maxSumOfPairs(arr, K):
    arr.sort()  # Sort the array to easily find valid pairs
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n):
        # Case 1: Not pairing arr[i], carry forward previous value
        dp[i + 1] = dp[i]

        # Case 2: Try pairing arr[i] with arr[i - 1] if their difference < K
        if arr[i] - arr[i - 1] < K:
            dp[i + 1] = max(dp[i + 1], dp[i - 1] + arr[i] + arr[i - 1])

    return dp[n]

# Example usage:
arr1 = [3, 5, 10, 15, 17, 12, 9]
K1 = 4
print("Maximum Sum of Pairs:", maxSumOfPairs(arr1, K1))  # Output: 62

arr2 = [5, 15, 10, 300]
K2 = 12
print("Maximum Sum of Pairs:", maxSumOfPairs(arr2, K2))  # Output: 25
