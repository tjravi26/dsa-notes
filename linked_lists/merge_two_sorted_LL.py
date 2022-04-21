# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list.
# Return the head of the new linked list.


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def mergeLists(head1, head2):
    # Create an empty node and assign a variable
    temp = dummy = SinglyLinkedListNode(0)
    while head1 and head2:
        if head1.data < head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next
    temp.next = head1 or head2
    return dummy.next  # Because dummy = 0 and dummy.next points to the head.
