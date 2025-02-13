class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Store next node
        current.next = prev  # Reverse pointer
        prev = current  # Move prev to current
        current = next_node  # Move current to next
    return prev  # New head of the reversed list


def reverse_linked_list_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


# Example Usage:
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("Original List:")
print_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed List:")
print_list(reversed_head)
