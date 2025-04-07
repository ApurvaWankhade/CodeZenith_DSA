class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def search(root, key):
    if root is None or root.val == key:
        return root is not None
    
    elif key > root.val:
        return search(root.right, key)

    return search(root.left, key)

# Example usage:
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

# Searching for a value
key = 7
print(search(root, key))  # Output: True

key = 14
print(search(root, key))  # Output: False