# Wrong Answer
# Python 2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def goleft(root):
    if root:
        print root.data,
        return goleft(root.left)
def goright(root):
    if root:
        print root.data,
        return goright(root.right)

def topView(root):
    if root.left:
        goleft(root.left)
    print root.data,
    if root.right:
        goright(root.right)

    
