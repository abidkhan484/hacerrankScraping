# Accepted
# Python 2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if not r:
        return Node(val)
    
    curr = r

    while curr.data:
        if val < curr.data:
            if not curr.left:
                curr.left = Node(val)
                break
            else:
                curr = curr.left
        elif val > curr.data:
            if not curr.right:
                curr.right = Node(val)
                break
            else:
                curr = curr.right
    
    return r
