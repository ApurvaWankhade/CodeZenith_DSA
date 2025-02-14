# Iterative Approach (Efficient)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1, l2):
    dummy = ListNode()  # Dummy node to simplify code
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach the remaining part of l1 or l2
    current.next = l1 if l1 else l2

    return dummy.next  # Head of merged list

# Recursive Approch

def merge_sorted_lists_recursive(l1, l2):
    if not l1: return l2
    if not l2: return l1

    if l1.val < l2.val:
        l1.next = merge_sorted_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_lists_recursive(l1, l2.next)
        return l2

# Example Usage:
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating sorted linked lists: 1 -> 3 -> 5 and 2 -> 4 -> 6
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))

print("List 1:")
print_list(l1)
print("List 2:")
print_list(l2)

merged_head = merge_sorted_lists(l1, l2)
print("Merged Sorted List:")
print_list(merged_head)


