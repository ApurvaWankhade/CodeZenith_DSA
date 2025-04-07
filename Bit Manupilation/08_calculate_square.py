#approch-1

def square(n):
    # Handle negative numbers
    if n < 0:
        n = -n  

    result = 0
    temp = n

    while temp > 0:
        result += n  # Repeated addition
        temp -= 1

    return result

# Test cases
print(square(5))   # Output: 25
print(square(7))   # Output: 49
print(square(12))  # Output: 144


# Approch-2: Bitwise Operator

def square(n):
    if n == 0:
        return 0

    # Handle negative numbers
    if n < 0:
        n = -n

    # Divide the number into two halves using bitwise shift
    x = n >> 1

    # Recursive formula: n^2 = 4*(x^2) + 4*x + 1 (if n is odd)
    if n & 1:
        return (square(x) << 2) + (x << 2) + 1
    else:
        return (square(x) << 2)

# Test cases
print(square(5))   # Output: 25
print(square(7))   # Output: 49
print(square(12))  # Output: 144

