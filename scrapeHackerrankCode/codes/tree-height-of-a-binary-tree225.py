# Wrong Answer
# Python 3

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root, p=0, maxim=-1):

    if root:
        if root.left:
            p = height(root.left, p+1, maxim)
            p -= 1
        if root.right:
            p = height(root.right, p+1, maxim)

        if p>maxim:
            maxim = p

    if not root:
        return maxim
    return p

