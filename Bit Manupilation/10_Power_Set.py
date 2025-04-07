# Approch-1

from itertools import combinations

def AllPossibleStrings(s):
    subsequences = []
    
    # Generate all non-empty subsequences using combinations
    for i in range(1, len(s) + 1):
        for combo in combinations(s, i):
            subsequences.append("".join(combo))
    
    # Sort the subsequences lexicographically
    subsequences.sort()
    
    return subsequences

# Test Cases
print(AllPossibleStrings("abc"))  # Output: ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
print(AllPossibleStrings("aa"))   # Output: ['a', 'a', 'aa']


# Approch-2

def AllPossibleStrings(s):
    n = len(s)
    subsequences = []

    # Iterate through all possible subsets (except empty set)
    for num in range(1, 1 << n):  # 1 to 2^n - 1
        sub = ""
        for i in range(n):
            if num & (1 << i):  # Check if the i-th bit is set
                sub += s[i]
        subsequences.append(sub)

    # Sort subsequences lexicographically
    subsequences.sort()
    
    return subsequences

# Test Cases
print(AllPossibleStrings("abc"))  # Output: ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
print(AllPossibleStrings("aa"))   # Output: ['a', 'a', 'aa']
