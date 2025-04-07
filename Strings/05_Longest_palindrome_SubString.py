class Solution:
    def longestPalindromeSubstring(self, s):
        def expand(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        longs = ""
        for i in range(len(s)):
            longs = max(longs, expand(i,i), expand(i,i+1), key=len)
        
        return longs
    
    
s = "babad"
sol = Solution()
print(sol.longestPalindromeSubstring(s))