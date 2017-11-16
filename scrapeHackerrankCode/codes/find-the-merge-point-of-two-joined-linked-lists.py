# Accepted
# Python 3

"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    while headA:
        check = headB
        while check:
            if headA.data == check.data:
                break
            check = check.next

        if check == None:
            headB = headB.next
            
        else:
            return check.data


        headA = headA.next
  
  
  
  
  
  
  
  
  
  

