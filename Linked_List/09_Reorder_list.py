# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):

        if not head or not head.next or not head.next.next:
            return

        # Step 1: Find the middle of the linked list (slow-fast pointer method)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow.next
        slow.next = None  # Cut off first half to prevent cycle
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge the first half and the reversed second half
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next  # Save next pointers
            first.next = second  # Link first node to second
            second.next = temp1  # Link second node to first's next
            first, second = temp1, temp2  # Move forward
