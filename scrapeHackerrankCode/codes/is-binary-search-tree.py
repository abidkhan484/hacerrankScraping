# Wrong Answer
# Python 2

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if not root:
        return True
        
    if root.left:
        if root.left.data <= root.data:
            return check_binary_search_tree_(root.left)
        else:
            return False
    if root.right:
        if root.right.data > root.data:
            return check_binary_search_tree_(root.right)
        else:
            return False
        
    return True

