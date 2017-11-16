# Wrong Answer
# Python 3

def checkBST(root):
    if root:
    
        if root.left:
    
    
            if root.left.data > root.data:
    
    
    
                print('No')
    
    
    
    
                return 'No'
    
    
    
    
            else:           
    
    
    
   
    
    
                checkBST(root.left)
    
    
    
    
                return 'Yes'
    
    
    
    
        if root.right:
    
    
            if root.right.data < root.data:
    
    
    
                print('No')
    
    
    
    
                return 'No'
    
    
    
    
            else:
    
    
    
                checkBST(root.right)
    
    
    
    
                return 'Yes'
    
    
    
    

