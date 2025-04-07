# Approch-1: Bitwise & Count Set Bits

import math

def findPosition(n):
    # Check if `n` has exactly one set bit (power of 2 check)
    if n <= 0 or (n & (n - 1)) != 0:
        return -1

    # Find position using log base 2
    return int(math.log2(n)) + 1

# Test Cases
print(findPosition(2))   # Output: 2 (10 in binary)
print(findPosition(5))   # Output: -1 (101 in binary)
print(findPosition(16))  # Output: 5 (10000 in binary)
print(findPosition(8))   # Output: 4 (1000 in binary)
print(findPosition(0))   # Output: -1


# Approch-2: Bitwise RIght Shift

def findPosition(n):
    # If `n` is not a power of 2, return -1
    if n <= 0 or (n & (n - 1)) != 0:
        return -1

    pos = 1
    while n > 1:
        n >>= 1  # Right shift `n` until the set bit reaches position 1
        pos += 1

    return pos

# Test Cases
print(findPosition(2))   # Output: 2
print(findPosition(5))   # Output: -1
print(findPosition(16))  # Output: 5
print(findPosition(8))   # Output: 4
print(findPosition(0))   # Output: -1





