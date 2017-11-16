# Wrong Answer
# Python 2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
    if root:
        print root.data,
        topView(root.right)


