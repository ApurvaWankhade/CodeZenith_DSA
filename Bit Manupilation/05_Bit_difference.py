# Approch-1: Using XOR and Counting Set Bits

def countFlippedBits(a, b):
    # XOR a and b to get differing bits
    xor_result = a ^ b

    # Count the number of set bits (1s) in xor_result
    return bin(xor_result).count('1')

# Test Cases
print(countFlippedBits(10, 20))  # Output: 4
print(countFlippedBits(20, 25))  # Output: 3
print(countFlippedBits(7, 15))   # Output: 1 (0111 to 1111, 1 flip needed)
print(countFlippedBits(0, 8))    # Output: 1 (0000 to 1000, 1 flip needed)


# Approch-2: Brian Kernighan’s Algorithm

def countFlippedBits(a, b):
    xor_result = a ^ b
    count = 0

    while xor_result:
        xor_result &= (xor_result - 1)  # Turn off the rightmost set bit
        count += 1

    return count

# Test Cases
print(countFlippedBits(10, 20))  # Output: 4
print(countFlippedBits(20, 25))  # Output: 3






