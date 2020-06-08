def detectLoop(head):
    marker1 = head
    marker2 = head
    
    while marker1 != None and marker2.next != None:
        marker1 = head.next
        marker2 = head.next.next
    
        if marker1 == marker2:
            return True
    return False