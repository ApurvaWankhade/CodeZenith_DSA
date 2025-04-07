class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = None
        self.right = None

def minimumOfBST(root):
    if root is None:
        return None
    
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr.val

# Example usage:
# Constructing the BST from the first example
#       5
#      / \
#     4   6
#    /     \
#   3       7
#  /
# 1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(1)

print(minimumOfBST(root))  # Output: 1