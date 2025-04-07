# Approch-1

def countSetBits(n):
    return bin(n).count('1')

# Test cases
print(countSetBits(6))  # Output: 2
print(countSetBits(8))  # Output: 1
print(countSetBits(3))  # Output: 2


# Approch-2

def countSetBits(n):
    count = 0
    while n:
        n &= (n - 1)  # Removes the rightmost 1-bit
        count += 1
    return count

# Test cases
print(countSetBits(6))  # Output: 2
print(countSetBits(8))  # Output: 1
print(countSetBits(3))  # Output: 2


# Approch-3

def countSetBits(n):
    count = 0
    while n:
        count += (n & 1)  # Check last bit
        n >>= 1  # Right shift by 1
    return count

# Test cases
print(countSetBits(6))  # Output: 2
print(countSetBits(8))  # Output: 1
print(countSetBits(3))  # Output: 2
