# Multiply two numbers represented by Linked Lists

MOD = 1000000007

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Multiply contents of two linked lists
def multiplyTwoLists(first, second):
    num1 = 0
    num2 = 0

    # Traverse the first list and 
    # construct the number with modulo
    while first is not None:
        num1 = (num1 * 10 + first.data) % MOD
        first = first.next

    # Traverse the second list and 
    # construct the number with modulo
    while second is not None:
        num2 = (num2 * 10 + second.data) % MOD
        second = second.next

    # Return the product of the two
    # numbers with modulo
    return (num1 * num2) % MOD


def printList(curr):
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next

if __name__ == "__main__":

    # Create first list 9->4->6
    head1 = Node(9)
    head1.next = Node(4)
    head1.next.next = Node(6)
    
    # Create second list 8->4
    head2 = Node(8)
    head2.next = Node(4)
    print(multiplyTwoLists(head1, head2))