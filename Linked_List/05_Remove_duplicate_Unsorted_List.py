class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

# Approach 1: Using a Hash Set

def removeDuplicates(head):
    if not head:
        return None

    seen = set()
    current = head
    seen.add(current.val)

    while current.next:
        if current.next.val in seen:
            current.next = current.next.next  # Skip duplicate node
        else:
            seen.add(current.next.val)
            current = current.next

    return head

# Approach 2: Using Two Loops (No Extra Space)

def removeDuplicatesNoExtraSpace(head):
    current = head

    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next  # Skip duplicate
            else:
                runner = runner.next
        current = current.next

    return head


