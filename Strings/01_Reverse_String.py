# 1. Using String Slicing (Pythonic way)

def reverse_string(s):
    return s[::-1]



# 2. Using reversed() and join()

def reverse_string(s):
    return ''.join(reversed(s))



# 3. Using a Loop (Iterative Approach)

def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev  # Adding characters in reverse order
    return rev


# 4. Using Recursion

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]


# 5. Using a List and pop() (Stack-like behavior)

def reverse_string(s):
    stack = list(s)
    rev = ''
    while stack:
        rev += stack.pop()
    return rev


# 6. Using collections.deque (Efficient for large strings)

from collections import deque

def reverse_string(s):
    dq = deque(s)
    rev = ''
    while dq:
        rev += dq.pop()
    return rev


# 7. Using reduce() from functools

from functools import reduce

def reverse_string(s):
    return reduce(lambda x, y: y + x, s)

print(reverse_string("hello"))  # Output: "olleh"