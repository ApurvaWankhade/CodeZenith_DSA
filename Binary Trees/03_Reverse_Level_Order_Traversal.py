from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseLevelOrder(self, root: TreeNode):
        if not root:
            return []

        queue = deque([root])
        stack = []  # Stack to reverse the order
        
        while queue:
            node = queue.popleft()
            stack.append(node.val)  # Push the node value into the stack
            
            # Enqueue right first, then left (so left appears first when reversed)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return stack[::-1]  # Reverse the stack to get bottom-up order

# Example Usage:
# Creating the tree [10, 20, 30, 40, 60]
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.left = TreeNode(40)
root.left.right = TreeNode(60)

sol = Solution()
print(sol.reverseLevelOrder(root))  # Output: [40, 60, 20, 30, 10]
