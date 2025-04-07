from collections import deque

# Node structure for the Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # Insert into the binary tree (level-order)
    def insert(self, key):
        new_node = TreeNode(key)
        if not self.root:
            self.root = new_node
            return
        
        queue = deque([self.root])
        while queue:
            temp = queue.popleft()
            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)
            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # Inorder Traversal (Left, Root, Right)
    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)

    # Preorder Traversal (Root, Left, Right)
    def preorder(self, node, result):
        if node:
            result.append(node.val)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    # Postorder Traversal (Left, Right, Root)
    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.val)

    # Level Order Traversal (BFS)
    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    # Depth First Search (DFS) - Iterative using stack
    def dfs_iterative(self):
        if not self.root:
            return []
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:  # Right first so that left is processed first
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # Search for a value in the tree using level order traversal
    def search(self, key):
        if not self.root:
            return False
        queue = deque([self.root])
        while queue:
            temp = queue.popleft()
            if temp.val == key:
                return True
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return False

# Example Usage:
if __name__ == "__main__":
    # Creating a sample binary tree:
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    tree = BinaryTree(root)

    inorder_result = []
    tree.inorder(root, inorder_result)
    print("Inorder Traversal:", inorder_result)

    preorder_result = []
    tree.preorder(root, preorder_result)
    print("Preorder Traversal:", preorder_result)

    postorder_result = []
    tree.postorder(root, postorder_result)
    print("Postorder Traversal:", postorder_result)

    print("Level Order Traversal (BFS):", tree.level_order())
    print("Depth First Search (DFS - Iterative):", tree.dfs_iterative())

    # Inserting a new node
    tree.insert(7)
    print("Level Order Traversal after insertion:", tree.level_order())

    # Searching for values
    print("Search 5:", tree.search(5))  # Output: True
    print("Search 10:", tree.search(10))  # Output: False
