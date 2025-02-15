def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Step 1: Find the first decreasing element from the right
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find the next larger element on the right
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the suffix (right part after index i)
    nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
