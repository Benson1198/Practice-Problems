def nth_to_last_node(n,head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        if not right_pointer.next:
            raise LookupError('n is larger than the Linked List')
        
        right_pointer = right_pointer.next
    
    while right_pointer.next:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next