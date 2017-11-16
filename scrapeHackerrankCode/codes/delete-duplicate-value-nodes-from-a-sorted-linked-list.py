# Accepted
# Python 3

"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    temp = head

    while temp:
        curr = temp.next
        i = 0
        while curr:
            if curr.data != temp.data:
                break

            curr = curr.next
        
        if curr != temp.next:
            temp.next = curr

        temp = temp.next

    return head
  
  
  
  
  
  
  
  
  
  

