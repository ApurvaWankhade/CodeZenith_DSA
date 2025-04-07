class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_dead_end(root):
    def helper(node, min_val, max_val):
        if not node:
            return False
        if min_val == max_val:
            return True
        return (helper(node.left, min_val, node.val - 1) or
                helper(node.right, node.val + 1, max_val))

    return helper(root, 1, float('inf'))

# Constructing the BST
#       8
#     /   \
#    5     9
#   / \
#  2   7
# /
#1

root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.left.left.left = TreeNode(1)

print(is_dead_end(root))  # Output: True


