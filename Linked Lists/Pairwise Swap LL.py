def pairWiseSwap(head):
    if head is None or head.next is None:
        return head
    temp = head
    while(temp is not None and temp.next is not None):
        temp1 = temp.data
        temp.data = temp.next.data
        temp.next.data = temp1
        temp= temp.next.next
    return head