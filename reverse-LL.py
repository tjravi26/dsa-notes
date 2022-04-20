def reverse(head):
    prev = None
    now = head

    while now != None:
        next = now.next
        now.next = prev
        prev = now
        now = next
    head = prev
    return head
  
  
  
  # See gif to understand
  https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Freverse-a-linked-list%2F&psig=AOvVaw3zfGTS7QCR98M5zvc8Bkrb&ust=1650542348844000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCIieyMfLovcCFQAAAAAdAAAAABAD
