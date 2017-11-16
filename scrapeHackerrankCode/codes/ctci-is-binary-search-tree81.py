# Wrong Answer
# Python 2

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def check(curr):
    p = True; q = True
    if curr.left:
        if curr.left.data > curr.data:
            p = False
    
    if curr.right:
        if curr.right.data < curr.data:
            q = False
            
    return p and q
    

def checkBST(root):
    
    if check(root):
        if root.left:
            return checkBST(root.left)
        if root.right:
            return checkBST(root.right)
    else:
        return False
    return True
