# Approch-1

def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0

# Test Cases
print(isPowerOfTwo(8))   # Output: True
print(isPowerOfTwo(98))  # Output: False
print(isPowerOfTwo(1))   # Output: True


# Approch-2

import math

def isPowerOfTwo(n):
    if n <= 0:
        return False
    return math.log2(n).is_integer()

# Test Cases
print(isPowerOfTwo(16))  # Output: True
print(isPowerOfTwo(18))  # Output: False


# Approch-3: Iterative divison by 2 (Brute Force)

def isPowerOfTwo(n):
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

# Test Cases
print(isPowerOfTwo(8))   # Output: True
