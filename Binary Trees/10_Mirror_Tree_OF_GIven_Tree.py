class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror_tree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left

    mirror_tree(root.left)
    mirror_tree(root.right)

    return root

def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left)+[root.val]+inorder_traversal(root.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

print("Inorder of original tree:", inorder_traversal(root))

mirror_tree(root)

print("Inorder of mirror tree:", inorder_traversal(root))
