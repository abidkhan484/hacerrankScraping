# Accepted
# Python 3

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    try:
        if head.next:
            return has_cycle(head.next)
        else:
            return 0
    except:
        return 1
    

