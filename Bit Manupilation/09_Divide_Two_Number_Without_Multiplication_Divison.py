# Approch-1

def divide(a, b):
    if a == 0:
        return 0
    
    # The sign will be negative only if sign of 
    # divisor and dividend are different
    sign = -1 if (a < 0) ^ (b < 0) else 1
    
    # Convert divisor and dividend to positive numbers
    a = abs(a)
    b = abs(b)
    
    # Initialize the quotient
    quotient = 0
    
    # Perform repeated subtraction till dividend
    # is greater than divisor
    while a >= b:
        a -= b
        quotient += 1
        
    return quotient * sign

if __name__ == "__main__":
    a = 43
    b = -8
    print(divide(a, b))



# Approch-2: Bitwise Operators

def divide(a: int, b: int) -> int:
    # Handle overflow case (only occurs for -2^31 / -1)
    INT_MAX, INT_MIN = (2**31 - 1, -2**31)
    if a == INT_MIN and b == -1:
        return INT_MAX  # Clamp to max 32-bit integer

    # Determine the sign of the result
    sign = -1 if (a < 0) ^ (b < 0) else 1  # XOR to check if only one is negative

    # Convert both numbers to positive
    a, b = abs(a), abs(b)

    quotient = 0

    # Iterate from most significant bit (31) to least (0)
    for i in range(31, -1, -1):
        if (b << i) <= a:  # Check if shifting `b` by `i` bits fits in `a`
            a -= (b << i)   # Subtract the shifted divisor from dividend
            quotient |= (1 << i)  # Add corresponding power of 2 to quotient

    return sign * quotient  # Apply the sign to the result


# Test Cases
if __name__ == "__main__":
    print(divide(43, -8))  # Output: -5
    print(divide(10, 3))   # Output: 3
    print(divide(-15, 2))  # Output: -7
    print(divide(1, 1))    # Output: 1







