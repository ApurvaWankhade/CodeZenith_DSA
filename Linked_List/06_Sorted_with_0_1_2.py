# Sorted a linked list of 0's 1s or 2s

# Approach 1: Counting Method

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def sortLinkedList(head):
    if not head:
        return None

    count = {0: 0, 1: 0, 2: 0}

    # Step 1: Count occurrences of 0s, 1s, and 2s
    current = head
    while current:
        count[current.val] += 1
        current = current.next

    # Step 2: Overwrite the list with counted values
    current = head
    for val in [0, 1, 2]:
        for _ in range(count[val]):
            current.val = val
            current = current.next

    return head


