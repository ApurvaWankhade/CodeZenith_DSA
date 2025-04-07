from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: Node):
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)  # Number of nodes at current level
            level_nodes = []  # Store node values for the current level
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.data)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)  # Append level to result

        return result

# Example Usage:
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

sol = Solution()
print(sol.levelOrder(root))  
# Output: [[3], [9, 20], [15, 7]]
