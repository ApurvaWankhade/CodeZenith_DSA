class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    # Step 1: Extract inorder traversal
    def storeInorder(self, root, inorder):
        if root is None:
            return
        self.storeInorder(root.left, inorder)
        inorder.append(root.data)
        self.storeInorder(root.right, inorder)

    # Step 2: Replace values from sorted order
    def arrayToBST(self, root, inorder_iterator):
        if root is None:
            return
        self.arrayToBST(root.left, inorder_iterator)
        root.data = next(inorder_iterator)
        self.arrayToBST(root.right, inorder_iterator)

    # Main function to convert binary tree to BST
    def binaryTreeToBST(self, root):
        if root is None:
            return None

        # Store the inorder traversal of the binary tree
        inorder = []
        self.storeInorder(root, inorder)

        # Sort the inorder values
        inorder.sort()

        # Replace values in original tree using sorted values
        self.arrayToBST(root, iter(inorder))

        return root

# Utility function for inorder traversal
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)

# Example Usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)

sol = Solution()
root = sol.binaryTreeToBST(root)

# Print inorder traversal of the converted BST
printInorder(root)  # Output: 1 2 3
