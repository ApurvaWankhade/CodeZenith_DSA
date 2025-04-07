# Python program to find the lps
# Returns the length of the longest 
# palindromic subsequence in seq
def lps(s, low, high):

    # Base case
    if low > high:
        return 0

    # If there is only 1 character
    if low == high:
        return 1

    # If the first and last characters match
    if s[low] == s[high]:
        return lps(s, low + 1, high - 1) + 2

    # If the first and last characters do not match
    return max(lps(s, low, high - 1), lps(s, low + 1, high))


def longestPalinSubseq(s):
    return lps(s, 0, len(s) - 1)


if __name__ == "__main__":
    s = "bbabcbcab"
    print(longestPalinSubseq(s))

#*******************************************************************************************************

# Python program to find the lps

# Function to find the LPS
def longestPalinSubseq(s):
    n = len(s)

    # Create a DP table
    dp = [[0] * n for _ in range(n)]

    # Build the DP table for all the substrings
    for i in range(n - 1, -1, -1):
        for j in range(i, n):

            # If there is only one character
            if i == j:
                dp[i][j] = 1
                continue

            # If characters at position i and j are the same
            if s[i] == s[j]:
                if i + 1 == j:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:

                # Otherwise, take the maximum length
                # from either excluding i or j
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The final answer is stored in dp[0][n-1]
    return dp[0][n - 1]

if __name__ == "__main__":
    s = "bbabcbcab"
    n = len(s)
    print(longestPalinSubseq(s))