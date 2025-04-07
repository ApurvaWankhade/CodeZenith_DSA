def canPartition(arr):
    total_sum = sum(arr)
    
    # If sum is odd, we can't partition into equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    n = len(arr)
    
    # DP array to check if sum j can be achieved with subset of arr
    dp = [False] * (target + 1)
    dp[0] = True  # A subset sum of 0 is always possible
    
    for num in arr:
        # Traverse backwards to avoid using the same number multiple times
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

# Example test cases
print(canPartition([1, 5, 11, 5]))  # Output: True
print(canPartition([1, 3, 5]))      # Output: False

#***************************************************************************************************************************

# Approch -2 

def canPartition(arr):
    total_sum = sum(arr)
    
    # If sum is odd, we can't partition into equal subsets
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    n = len(arr)
    
    # DP Table: dp[i][j] => True if we can form sum j using first i elements
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    
    # We can always form sum 0 by picking no elements
    for i in range(n + 1):
        dp[i][0] = True  

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]  # Cannot include current element
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]  # Include or exclude
    
    return dp[n][target]

# Example test cases
print(canPartition([1, 5, 11, 5]))  # Output: True
print(canPartition([1, 3, 5]))      # Output: False


