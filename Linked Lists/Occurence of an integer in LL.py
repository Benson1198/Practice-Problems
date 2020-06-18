def count(head, search_for):
    count = 0
    t = head
    
    while t != None:
        if t.data == search_for:
            count += 1
        t = t.next
    
    return count