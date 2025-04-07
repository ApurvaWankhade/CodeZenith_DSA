class Solution(object):
    def maxProduct(self, nums):
        result = float('-inf')
        n = len(nums)
        prefix = 1
        sufix = 1
        
        for i in range(n):
            if prefix == 0: 
                prefix = 1
            if sufix == 0: 
                sufix = 1

            prefix *= nums[i]
            sufix *= nums[n - i - 1]

            result = max(result, prefix, sufix)
        
        return result


nums = [0,2]
sol = Solution()
print(sol.maxProduct(nums))  # Expected Output: 2
