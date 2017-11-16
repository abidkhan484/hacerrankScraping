# Accepted
# Python 3

def MergeLists(headA, headB):
    if headA is None or headB is None:
        return headA or headB
    
    if headA.data < headB.data:
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next
        
    curr = head
    
    while headA or headB:
        if not headA or not headB:
            curr.next = headA or headB
            return head
        if headA.data < headB.data:
            curr.next = headA
            headA = headA.next
        else:
            curr.next = headB
            headB = headB.next
        curr = curr.next
        
    return head

