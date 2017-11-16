# Accepted
# Python 2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    #Write your code here
    curr = root
    if not root:
        return
    if curr:
        print curr.data,
        preOrder(curr.left)
        preOrder(curr.right)

