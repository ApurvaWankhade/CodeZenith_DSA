from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_view(root):
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

        # Add left child first, then right child
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return result

# Example Usage:
# Constructing the binary tree for input: [1, 2, 3, 4, 5, N, N]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(left_view(root))  # Output: [1, 2, 4]
