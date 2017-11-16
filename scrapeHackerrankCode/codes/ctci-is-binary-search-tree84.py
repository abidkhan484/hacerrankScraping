# Wrong Answer
# Python 2

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):

    if root.left:
        if root.left.data < root.data:
            checkBST(root.left)
        else:
            return False
    if root.right:
        if root.right.data > root.data:
            checkBST(root.right)
        else:
            return False
            
    return True
