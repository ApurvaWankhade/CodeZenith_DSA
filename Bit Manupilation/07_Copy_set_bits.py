def copySetBitsInRange(x, y, l, r):
    # Create a mask with set bits in the given range [l, r]
    mask = ((1 << (r - l + 1)) - 1) << (l - 1)
    
    # Extract the bits of 'y' in this range
    set_bits = y & mask  
    
    # Copy these bits to 'x'
    x = x | set_bits  

    return x

# Test cases
print(copySetBitsInRange(10, 13, 2, 3))  # Output: 14
print(copySetBitsInRange(8, 7, 1, 2))    # Output: 11
