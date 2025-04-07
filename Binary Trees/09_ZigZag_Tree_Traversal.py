from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True  # Flag for direction
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            
            # Enqueue children left to right
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Reverse order for right-to-left levels
        if not left_to_right:
            level_nodes.reverse()
        
        result.extend(level_nodes)
        left_to_right = not left_to_right  # Toggle direction

    return result

# Example Usage:
# Constructing the binary tree for input:
#         1
#       /   \
#      2      3
#     / \    /  \
#    4   5  6    7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(zigzag_level_order(root))  # Output: [1, 3, 2, 4, 5, 6, 7]
