def addBoth(head_a,head_b):
    resultant = LinkedList()
    curr_a = head_a
    curr_b = head_b

    carry = 0 #Variable to store carry over

    while curr_a and curr_b :
        temp_res = curr_a.data + curr_b.data + carry
        carry = temp_res // 10
        temp_res =temp_res%10
        resultant.append(temp_res)
        curr_b = curr_b.next
        curr_a = curr_a.next

    while curr_a :
        temp_res = curr_a.data + carry
        carry = temp_res // 10
        temp_res =temp_res%10
        resultant.append(temp_res)
        curr_a = curr_a.next

    while curr_b :
        temp_res = curr_b.data + carry
        carry = temp_res // 10
        temp_res =temp_res%10
        resultant.append(temp_res)
        curr_b = curr_b.next
    
    if carry:
        resultant.append(carry)
    
    #if any carry is remaining
    return  resultant.head