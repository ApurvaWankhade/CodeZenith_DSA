class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_predecessor_successor(root, key):
    predecessor = None
    successor = None
    current = root

    while current:
        if current.key == key:
            # Find predecessor (rightmost node in left subtree)
            if current.left:
                temp = current.left
                while temp.right:
                    temp = temp.right
                predecessor = temp

            # Find successor (leftmost node in right subtree)
            if current.right:
                temp = current.right
                while temp.left:
                    temp = temp.left
                successor = temp
            break

        elif key < current.key:
            successor = current
            current = current.left
        else:
            predecessor = current
            current = current.right

    return (predecessor.key if predecessor else None,
            successor.key if successor else None)

# Example Usage:
# Constructing the BST from the first example
#       8
#     /   \
#    1     9
#     \     \
#      4     10
#     /
#    3
root = TreeNode(8)
root.left = TreeNode(1)
root.right = TreeNode(9)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.right.right = TreeNode(10)

key = 8
predecessor, successor = find_predecessor_successor(root, key)
print(f"Key: {key}, Predecessor: {predecessor}, Successor: {successor}")
# Output: Key: 8, Predecessor: 4, Successor: 9
