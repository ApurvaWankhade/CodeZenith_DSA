from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_view(root):
    if not root:
        return []
    
    result = []
    queue = deque([(root, 0)])  # (node, level)
    visited_levels = set()

    while queue:
        node, level = queue.popleft()

        # If this is the first node of the level, add it to the result
        if level not in visited_levels:
            result.append(node.val)
            visited_levels.add(level)

        # Add right child first, then left child
        if node.right:
            queue.append((node.right, level + 1))
        if node.left:
            queue.append((node.left, level + 1))

    return result

# Example Usage:
# Constructing the binary tree for input: [10, 20, 90, 40, 60]
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(90)
root.left.left = TreeNode(40)
root.left.right = TreeNode(60)

print(right_view(root))  # Output: [10, 90, 60]


