def longestSubsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize all lengths to 1

    for i in range(1, n):
        for j in range(i):
            if abs(arr[i] - arr[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Return the maximum length found

# Example Test Cases
arr1 = [10, 9, 4, 5, 4, 8, 6]
print("Output:", longestSubsequence(arr1))  # Output: 3

arr2 = [1, 2, 3, 4, 5]
print("Output:", longestSubsequence(arr2))  # Output: 5
