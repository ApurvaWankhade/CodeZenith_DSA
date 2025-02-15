#User function Template for python3

def knapSack(self, val, wt,capacity):
    # code here
    dp = [0] * (capacity + 1)

    for i in range(capacity + 1):
        for j in range(len(wt)):
            if wt[j] <= i:
                dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
    
    return dp[capacity]
    


# Example usage
wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
capacity = 5
print(knapSack(wt, val, capacity))  # Output: 7