''' Valid Parentheses '''

# Stack Implementation - Efficient Approch

def is_valid_parentheses(s):
    matchp={']':'[','}':'{',')':'('}
    stack=[]
    
    for char in s:
        if char in matchp.values():
            stack.append(char)
        elif char in matchp:
            if not stack or stack.pop()!=matchp[char]:
                return False
        else:
            return False
    return len(stack)==0


def is_valid(s):
    stack = []
    # Mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map:         # If it's a closing bracket
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            return False  # Invalid character found

    return not stack  # Return True if the stack is empty