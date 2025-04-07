class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None
    
def lowestCommonAncestor(root, p, q):
    if root is None:
        return None
    
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    
    else:
        return root

# Example BST Construction
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Test Cases
p = root.left  # Node with value 2
q = root.right  # Node with value 8
print(lowestCommonAncestor(root, p, q).val)  # Output: 6

p = root.left  # Node with value 2
q = root.left.right  # Node with value 4
print(lowestCommonAncestor(root, p, q).val)  # Output: 2
    
