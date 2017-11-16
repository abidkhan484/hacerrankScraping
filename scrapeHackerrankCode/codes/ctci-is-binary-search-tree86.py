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
    li = [root]
    while li:
        if li[0].left:
            if li[0].data > li[0].left.data:
                li.append(li[0].left)
            else:
                return False
        if li[0].right:
            if li[0].data < li[0].right.data:
                li.append(li[0].right)
            else:
                return False
        del li[0]
    return True

