class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: Node):
        if not root:
            return None

        # Swap left and right subtrees
        root.left, root.right = root.right, root.left  

        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root  # Return the modified tree root

# Helper function to print level order
def level_order_traversal(root):
    if not root:
        return []
    
    from collections import deque
    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.data)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Example Usage
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

sol = Solution()
inverted_root = sol.invertTree(root)
print(level_order_traversal(inverted_root))  # Output: [4, 7, 2, 9, 6, 3, 1]
