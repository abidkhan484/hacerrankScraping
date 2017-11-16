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
    if not root:
        return True
    else:
        if root.left:
            if root.left.data < root.data:
                return checkBST(root.left)
            else:
                return False
        if root.right:
            if root.right.data > root.data:
                return checkBST(root.right)
            else:
                return False
            
    return True
