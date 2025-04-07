class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Function to check if two trees are identical
    def isIdentical(self, root1, root2):
        if not root1 and not root2:
            return True  # Both trees are empty
        if not root1 or not root2:
            return False  # One tree is empty
        if root1.val != root2.val:
            return False  # Values do not match

        # Recursively check left and right subtrees
        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)

    # Function to check if subRoot is a subtree of root
    def isSubtree(self, root, subRoot):
        if not root:
            return False  # Reached the end, no match found
        if self.isIdentical(root, subRoot):
            return True  # Found identical subtree

        # Recursively check left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# Example Usage:
# Creating the tree root = [3,4,5,1,2]
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

# Creating subRoot = [4,1,2]
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

sol = Solution()
print(sol.isSubtree(root, subRoot))  # Output: True
