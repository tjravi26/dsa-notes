# When two LLs are given with input as the head, compare the two and return 1 if the lists are equal. Otherwise, return 0.


def compare_lists(head1, lhead2):
    while head1 and head2:
        if head1.data == head2.data:
            head1 = head1.next
            head2 = head2.next
        else:
            return 0

    if head1 is None and head2 is None:
        return 1
    else:
        return 0
