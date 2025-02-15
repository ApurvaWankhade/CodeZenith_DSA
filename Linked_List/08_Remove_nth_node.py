# Two-Pass Approach
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head, n):

    dummy = ListNode(0, head)
    current = head
    length = 0

    # First pass: Calculate the length of the linked list
    while current:
        length += 1
        current = current.next

    # Find the position to remove (from the start)
    target = length - n
    current = dummy

    # Move to the node just before the target
    for _ in range(target):
        current = current.next

    # Remove the nth node
    current.next = current.next.next

    return dummy.next