# Accepted
# Python 2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    #Write your code here
    if not root:
        return
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print root.data,

