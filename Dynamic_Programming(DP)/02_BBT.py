def countBT(self, h):
    # code here 
    if h==0:
        return 1
    if h==1:
        return 1
    dp =[0] * (h+1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, h+1):
        dp[i] = dp[i-1]*dp[i-1] + 2*dp[i-1]*dp[i-2]

    
    return dp[h]