class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def deleteNode(node):
    if node is None or node.next is None:
        return

    node.val = node.next.val  # Copy the next node’s value
    node.next = node.next.next  # Bypass the next node

# Example Usage:

def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating linked list: 4 -> 5 -> 1 -> 9 -> None
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

print("Original List:")
printList(head)

# Deleting node with value 5 (assuming we have access to it directly)
deleteNode(head.next)

print("After Deleting Node 5:")
printList(head)
