def reverseList(self):
    if self.head is None:
        return None
    prev = None
    curr = self.head
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    self.head = prev