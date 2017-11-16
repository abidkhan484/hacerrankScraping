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
def height2(root, p=0, maxim=-1):

    if root:
        if root.left:
            p, maxim = height2(root.left, p+1, maxim)
            p -= 1
        if root.right:
            p, maxim = height2(root.right, p+1, maxim)

        if maxim<p:
            maxim = p

    return p, maxim

def height(root):
    return height2(root)[-1]

