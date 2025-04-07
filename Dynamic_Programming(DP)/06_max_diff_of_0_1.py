def maxSubstring(S):
    max_sum = float('-inf')
    current_sum = 0
    all_ones = True  # To check if all elements are 1s

    for ch in S:
        value = 1 if ch == '0' else -1  # Convert 0 → +1, 1 → -1
        current_sum += value

        # Check if we got at least one '0'
        if ch == '0':
            all_ones = False

        # Apply Kadane’s Algorithm
        if current_sum < 0:
            current_sum = 0

        max_sum = max(max_sum, current_sum)

    return -1 if all_ones else max_sum

# Example Test Cases
print(maxSubstring("11000010001"))  # Output: 6
print(maxSubstring("111111"))       # Output: -1
