def longestValidParentheses(s):
    stack = [-1]  # Initialize stack with -1 to handle edge cases
    max_length = 0  # Stores max length of valid substring

    for i in range(len(s)):
        if s[i] == '(':  # Push index of '(' onto the stack
            stack.append(i)
        else:  # When ')' is encountered
            stack.pop()  # Pop last '(' index

            if not stack:  # If stack becomes empty, push current index as base
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])  # Calculate valid length
        
    return max_length

# Example Test Cases
print(longestValidParentheses("((()"))     # Output: 2
print(longestValidParentheses(")()())"))   # Output: 4
print(longestValidParentheses("()(()))"))  # Output: 6
