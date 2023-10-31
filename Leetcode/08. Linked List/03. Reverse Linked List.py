class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def printLinkedList(head):
    while head is not None:
        print(head.val)
        head = head.next
    print("None")

head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head1 = reverseLinkedList(head1)
printLinkedList(reversed_head1)
