# Accepted
# Python 3

"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if position==0:
        return head.next
    start = head
    prev = head
    while position >= 1:
        prev = head
        head = head.next
        position -= 1
    prev.next = head.next
    return start
  
  
  
  

