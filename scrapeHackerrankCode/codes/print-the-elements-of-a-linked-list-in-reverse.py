# Accepted
# Python 3

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    current = head        
    li = []
    while current:
        li.append(current.data)            
        current = current.next
    l = len(li)-1
    for i in range(l, -1, -1):
        print(li[i])


