# Approach-1: Naive Approach (Loop through each number)

def countSetBitsNaive(n):
    count = 0
    for i in range(1, n+1):
        count += bin(i).count('1')
    
    return count

# Test Cases
print(countSetBitsNaive(4))   # Output: 5
print(countSetBitsNaive(17))  # Output: 35


# Approch-2: Optimized Approach (Using Bitwise Pattern)

import math

def countSetBits(n):
    if n == 0:
        return 0

    # Find the highest power of 2 ≤ n
    x = int(math.log2(n))

    # Total set bits from 1 to 2^x - 1
    bits_up_to_2x = x * (1 << (x - 1))  # x * 2^(x-1)

    # Count remaining set bits
    msb_2x_to_n = n - (1 << x) + 1  # Most significant bits from 2^x to n

    # Recursively count for the remaining numbers
    rest = countSetBits(n - (1 << x))

    return bits_up_to_2x + msb_2x_to_n + rest

# Test Cases
print(countSetBits(4))   # Output: 5
print(countSetBits(17))  # Output: 35












