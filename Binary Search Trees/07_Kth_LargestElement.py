class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    def inorder(self, root, elements):
        """Perform inorder traversal and store elements in a list."""
        if root is None:
            return
        self.inorder(root.left, elements)
        elements.append(root.data)
        self.inorder(root.right, elements)

    def kthLargest(self, root, k):
        """Find the k-th largest element using inorder traversal."""
        elements = []
        self.inorder(root, elements)
        return elements[-k]  # Get k-th largest from the end of sorted list

# Example Usage:
root = Node(4)
root.left = Node(2)
root.right = Node(9)

sol = Solution()
print(sol.kthLargest(root, 2))  # Output: 4
print(sol.kthLargest(root, 1))  # Output: 9
print(sol.kthLargest(root, 3))  # Output: 2
