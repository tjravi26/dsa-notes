# Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list.
# Return the head of the new linked list.


def mergeLists(head1, head2):
    # Both lists are None
    if head1 is None and head2 is None:
        return None

    # Only one list is None
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # General logic
    if head1.data < head2.data:
        temp = head1
        temp.next = mergeLists(head1.next, head2)
    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next)
    return temp
