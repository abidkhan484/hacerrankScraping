# Accepted
# Python 3

    def removeDuplicates(self,head):
        curr = head
        while curr.next:
            if curr.data != curr.next.data:
                curr = curr.next
            else:
                tmp = curr.next
                while tmp.next:
                    if curr.data==tmp.next.data:
                        tmp = tmp.next
                    else:
                        break
                curr.next = tmp.next
  
        return head
  
  
  
  
  
  
  
  
  
