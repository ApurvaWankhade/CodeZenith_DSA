''' Valid Palindrome '''

# Approch-1

def validpalin(s):
    cleaned_str = ""
    for char in s:
        if char.isalnum():
            cleaned_str += char.lower()
    return cleaned_str == cleaned_str[::-1]

def validpalin(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s==s[::-1]


# Approch-2

# Two-pointer approach

def validpalin(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric characters
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        # Compare characters (case-insensitive)
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True

# Approch-3

# Using regular expressions

import re

def validpalin(s):
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned_str == cleaned_str[::-1]

# Approch-4
# Using Stack

def validpalin(s):
    stack = []
    for char in s:
        if char.isalnum():
            stack.append(char.lower())

    for char in s:
        if char.isalnum():
            if stack.pop() != char.lower():
                return False
    return True


# Approch-5
# Using filter() and reversed()

def is_palindrome(s):
    filtered = ''.join(filter(str.isalnum, s)).lower()
    return filtered == ''.join(reversed(filtered))