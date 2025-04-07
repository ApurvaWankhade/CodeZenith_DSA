class Solution(object):
    def minDistance(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i  # Removing all characters from s1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters to s1

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:  # If characters match, no edit needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],    # Remove
                                       dp[i][j - 1],    # Insert
                                       dp[i - 1][j - 1]) # Replace

        return dp[m][n]

# Example usage:
sol = Solution()
print(sol.minDistance("geek", "gesek"))  # Output: 1
print(sol.minDistance("gfg", "gfg"))     # Output: 0
print(sol.minDistance("abc", "def"))     # Output: 3
