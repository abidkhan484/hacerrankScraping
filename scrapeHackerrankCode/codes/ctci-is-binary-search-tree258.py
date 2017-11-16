# Wrong Answer
# Python 3

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    if root:
        if root.left:
            if root.left.data > root.data:
                return 'No'
            checkBST(root.left)
        if root.right:
            if root.right.data < root.data:
                return 'No'
            checkBST(root.right)
            
        return 'Yes'
    else:
        return 'Yes'

