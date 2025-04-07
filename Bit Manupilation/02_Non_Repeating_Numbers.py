class Solution:
    def singleNumber(self, arr):
        # Using a set to track elements
        seen = set()
        
        for i in arr:
            if i in seen:
                seen.remove(i)  # Remove if already present (pair completed)
            else:
                seen.add(i)  # Add if seen for the first time
        
        return sorted(seen)  # Return numbers in increasing order

# Example usage
sol = Solution()
print(sol.singleNumber([1, 2, 3, 2, 1, 4]))  # Output: [3, 4]
print(sol.singleNumber([2, 1, 3, 2]))        # Output: [1, 3]
print(sol.singleNumber([2, 1, 3, 3]))        # Output: [1, 2]


# Approch-2

def findTwoUniqueNumbers(arr):
    xor_result = 0
    
    # Step 1: XOR all numbers, duplicate pairs cancel out
    for num in arr:
        xor_result ^= num
    
    # Step 2: Find the rightmost set bit
    diff = xor_result & -xor_result
    
    x = y = 0  # Two unique numbers
    
    # Step 3: Divide numbers into two groups
    for num in arr:
        if num & diff:
            x ^= num  # Group 1 (bit is set)
        else:
            y ^= num  # Group 2 (bit is not set)
    
    # Step 4: Return the numbers in increasing order
    return sorted([x, y])

# Test Cases
print(findTwoUniqueNumbers([1, 2, 3, 2, 1, 4]))  # Output: [3, 4]
print(findTwoUniqueNumbers([2, 1, 3, 2]))        # Output: [1, 3]
print(findTwoUniqueNumbers([2, 1, 3, 3]))        # Output: [1, 2]


# Approch-3: Using Hashing

from collections import Counter

def findTwoUniqueNumbers(arr):
    freq = Counter(arr)  # Count occurrences of each number
    result = [num for num in freq if freq[num] == 1]
    return sorted(result)  # Return in increasing order

# Test Cases
print(findTwoUniqueNumbers([1, 2, 3, 2, 1, 4]))  # Output: [3, 4]
print(findTwoUniqueNumbers([2, 1, 3, 2]))        # Output: [1, 3]
print(findTwoUniqueNumbers([2, 1, 3, 3]))        # Output: [1, 2]



