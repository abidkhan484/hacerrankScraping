# Wrong Answer
# Python 2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
    
    curr = root; li = []; li2 = []
    while curr:
        if curr.data != v1:
            li.append(curr.data)
        else:
            break
        if curr.data > v1:
            curr = curr.left
        else:
            curr = curr.right
    
    curr = root
    while curr:
        if curr.data != v2:
            li2.append(curr.data)
        else:
            break
        if curr.data > v2:
            curr = curr.left
        else:
            curr = curr.right
    
    l = min(len(li), len(li2))
    if l == 0:
        return root
    for i in range(l):
        if li[i]==li2[i]:
            f = li[i]
        else:
            break
    
    curr = root
    while curr:
        if curr.data==f:
            return curr
        if curr.data > f:
            curr = curr.left
        else:
            curr = curr.right

