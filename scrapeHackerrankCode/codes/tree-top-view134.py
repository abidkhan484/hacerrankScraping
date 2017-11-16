# Accepted
# Python 2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
    li = []; curr = root
    while root:
        li.append(root.data)
        root = root.left
    
    li.reverse()
    
    curr = curr.right
    while curr:
        li.append(curr.data)
        curr = curr.right
        
    i = 0
    while i<len(li):
        print li[i],
        i += 1

