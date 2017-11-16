# Accepted
# Python 2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    
    if not root:
        return
    li = [root]
    while li:
        print li[0].data, 
        if li[0].left:
            li.append(li[0].left)
        if li[0].right:
            li.append(li[0].right)
        del li[0]


