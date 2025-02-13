# Detect Cycle in a Linked List (Floyd’s Algorithm)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # Move one step
        fast = fast.next.next      # Move two steps
        if slow == fast:           # Cycle detected
            return True
    return False  # No cycle found

# Example Usage:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creating a cycle

print(has_cycle(node1))  # Output: True
